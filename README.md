# Cricket Stats Data Pipeline Project
This project is designed to fetch cricket stats data from an API, process the data, and load it into Google Cloud Storage (GCS) and Google BigQuery for further analysis. The pipeline is fully automated, orchestrated using Google Cloud Composer (Airflow), and scheduled to run daily.

## Problem Statement
The goal is to automate the collection, transformation, and loading of cricket statistics data for users who require up-to-date cricket stats. This pipeline ensures the data is regularly fetched, processed, and stored in a structured format for quick consumption and analysis.

## Architecture Diagram
![image](https://github.com/user-attachments/assets/19018523-f777-4ae3-909f-64ef17cd92af)


## Technologies Used
Google Cloud Composer (Airflow): For orchestration and scheduling.
Google Cloud Storage (GCS): For storing the transformed CSV data.
Google BigQuery: For data warehousing and analysis.
Python: For data extraction, transformation, and loading.
RapidAPI: Source for the cricket stats data.

## Project Structure

![Project Structure](https://github.com/user-attachments/assets/809dffc9-88c3-4710-9484-1306d9df913b)

## Pipeline Overview
## 1. Data Extraction and Transformation:
The pipeline fetches cricket stats (like batsmen rankings) using the Cricbuzz API from RapidAPI.
The extracted data is processed and transformed into a CSV format with fields like rank, name, and country.
The processed CSV file is uploaded to a GCS bucket.
## 2. Data Loading to BigQuery:
The CSV file stored in GCS is loaded into a BigQuery table.
The table schema is predefined to ensure accurate data loading and prevent schema-related issues.

## Key Features
Fully Automated: The pipeline runs daily without manual intervention.
Orchestrated and Scheduled: Google Cloud Composer is used to manage task dependencies and scheduling.
Scalable and Flexible: The pipeline can be easily extended to handle more data sources or different types of cricket stats.

## How to Run
Clone this repository:
git clone https://github.com/ironfist1769/cricket-pipeline

## Navigate to the project directory:
cd cricket-stats-pipeline

## Deploy the Airflow DAG:
Upload the `dags_cricket_etl_pipeline.py` file to your Composer environment.

## Create the necessary modules:
Place the Python modules (`dags_modules_Data_Load_BQ.py` and `dags_modules_extract_and_push_gcs.py`) in the appropriate path for Airflow to access.

## Configure API and GCP credentials:

Ensure you have the correct API keys and Google Cloud credentials set up in your environment.
## Trigger the DAG:

You can either run the DAG manually or let it run as scheduled (daily).

## Detailed Code Explanation
Airflow DAG: dags/dags_cricket_etl_pipeline.py
This DAG orchestrates the entire ETL pipeline. It includes tasks for fetching and transforming the cricket data, followed by loading it into BigQuery.

Module 1: modules/dags_modules_extract_and_push_gcs.py
This script handles the extraction of data from the API, transformation into CSV format, and uploading the CSV to GCS.

Module 2: modules/dags_modules_Data_Load_BQ.py
This script loads the CSV data stored in GCS into a BigQuery table with a predefined schema.

## Intended Audience
Data Analysts and Cricket Enthusiasts interested in up-to-date cricket stats.
Developers looking for a reference implementation of a cloud-based data pipeline.
## Future Enhancements
Add support for more data types (e.g., bowling stats, team rankings).
Implement error handling and data validation.
Introduce monitoring and logging for better observability.
