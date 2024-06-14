import requests
import pandas as pd
from typing import List, Dict, Any

class NobelPrizeExtractor:
    base_url: str
    params: Dict[str, Any]
    nobel_prizes: List[Dict[str, Any]]
    prizes_df: pd.DataFrame
    laureates_df: pd.DataFrame
    prize_laureates_df: pd.DataFrame

    def __init__(self) -> None:
        self.base_url = "https://api.nobelprize.org/2.1/nobelPrizes"
        self.params = {"offset": 0, "limit": 1000, "csvLang": "en"}
        self.nobel_prizes = []
        self.prizes_df = pd.DataFrame()
        self.laureates_df = pd.DataFrame()
        self.prize_laureates_df = pd.DataFrame()
        
    def extract_nobel_prize(self) -> None:
        try:
            while True:
                response: requests.Response = requests.get(self.base_url, params=self.params)
                response.raise_for_status()
                data: Dict[str, Any] = response.json()
                self.nobel_prizes.extend(data["nobelPrizes"])
                if len(data["nobelPrizes"]) < self.params["limit"]:
                    break

                self.params["offset"] += self.params["limit"]
        
        except (requests.exceptions.RequestException, ValueError, KeyError) as err:
            print(f"An error occurred: {err}")
        
    def transform_data(self) -> None:
        self.transform_prizes()            # prizes.csv      
        self.transform_laureates()         # laureates.csv
        self.transform_prize_laureates()   # prize_laureates.csv

    def transform_prizes(self) -> None:
        self.prizes_df = pd.json_normalize(self.nobel_prizes)
        self.prizes_df = self.prizes_df[["awardYear", "category.en", "prizeAmount", "prizeAmountAdjusted"]]
        self.prizes_df.columns = ["award_year", "category", "prize_amount", "prize_amount_adjusted"]

    def transform_laureates(self) -> None:
        laureates_list: List[Dict[str, Any]] = []
        for prize in self.nobel_prizes:
            if 'laureates' in prize:
                for laureate in prize["laureates"]:
                    laureates_list.append({
                        "id": laureate["id"],
                        "known_name": laureate.get("knownName", {}).get("en"),
                        "full_name": laureate.get("fullName", {}).get("en"),
                        "motivation": laureate.get("motivation", {}).get("en"),
                        "award_year": prize["awardYear"],
                        "category": prize["category"]["en"]
                    })
        
        if laureates_list:
            self.laureates_df = pd.DataFrame(laureates_list).drop_duplicates()
        else:
            print("No laureates data found in the fetched Nobel Prizes.")

    def transform_prize_laureates(self) -> None:
        prize_laureates_list: List[Dict[str, Any]] = [{
            "award_year": prize["awardYear"],
            "category": prize["category"]["en"],
            "laureate_id": laureate["id"]
        } for prize in self.nobel_prizes if 'laureates' in prize for laureate in prize["laureates"]]
        
        self.prize_laureates_df = pd.DataFrame(prize_laureates_list).drop_duplicates()

    def save_data(self) -> None:
        self.prizes_df.to_csv("/opt/airflow/data/prizes.csv", index=False)
        self.laureates_df.to_csv("/opt/airflow/data/laureates.csv", index=False)
        self.prize_laureates_df.to_csv("/opt/airflow/data/prize_laureates.csv", index=False)
        print("Data extraction and transformation complete. CSV files have been saved.")

    def execute(self) -> None:
        self.extract_nobel_prize()
        self.transform_data()
        self.save_data()