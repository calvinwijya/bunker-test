# Project Roadmap

## Project Vision
Setup an ETL pipeline to extract data from [Nobel Prize API](https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1#/default/get_nobelPrizes), transform the dataset in 3NF and store the data to somewhere the enable us to easy to query or explore

## Current Project Details
### Data Extraction
- **Source**: [Nobel Prize API](https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1#/default/get_nobelPrizes)
- **Process**: Extract data from the API and save it into a CSV file.
- **Tools**: Python, Airflow, Pandas

### Data Exploration
- **Environment**: Jupyter Notebook
- **Tools**: Apache Spark, 
- **Process**: Load the CSV file into Spark, perform data exploration and provide SQL for transformation

## Future Improvements
### 1. Separate ETL Process Repository
- **Objective**: Modularize the project by creating a dedicated repository for the ETL process.
- **Benefits**: Improved code organization, easier maintenance, and better collaboration.

### 2. Load Data to a Lakehouse (e.g Databricks)
- **Objective**: Load the extracted data into a lakehouse platform like Databricks for more scalable and efficient data management.
- **Benefits**: Enhanced scalability, performance, and data governance.

### 3. Use dbt for Transformation Pipeline
- **Objective**: Implement dbt (data build tool) to manage the data transformation pipeline using SQL.
- **Benefits**: Simplifies complex data transformations, ensures better data quality, and provides clear documentation of data transformations.

### 6. Implement Data Quality Checks
- **Objective**: Add data quality checks to ensure the accuracy and consistency of the data.
- **Benefits**: Detects and prevents data anomalies, improves data reliability, and maintains data integrity.
