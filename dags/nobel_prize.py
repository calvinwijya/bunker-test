from airflow import DAG
from airflow.operators.python import PythonOperator
from extractor.nobel_prize_extractor import NobelPrizeExtractor


from datetime import datetime

with DAG('nobel_prize', start_date=datetime(2024, 6, 14), schedule_interval='@daily', catchup=False) as DAG:

    run_my_function = PythonOperator(
        task_id='extract_nobel_prize',
        python_callable=NobelPrizeExtractor().execute,
        provide_context=True,
    )

    run_my_function