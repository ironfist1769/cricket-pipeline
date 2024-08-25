from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from google.cloud import storage, bigquery
import requests
import csv

from modules.Data_Load_BQ import load_csv_to_bigquery
from modules.extract_and_push_gcs import generate_csv_and_load_csv_to_storage


url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"
headers = {
            "x-rapidapi-key": "2a40e211d1msh5f1ffd560588031p10ed73jsnd27dc3489ec5",
            "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
        }
csv_filename = 'batsmen_rankings.csv'
bucket_name = 'file-dump-practise'
file_name = "batsmen_rankings.csv"
dataset_id = "practice-1-433516.sandbox"
table_id = "cricketer_stats"


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 8, 25),
    'depends_on_past': False,
    'email': ['animatedstudios40@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('fetch_cricket_stats',
          default_args=default_args,
          description='Runs an external Python script',
          schedule_interval='@daily',
          catchup=False)

load_cricket_data_to_gcs = PythonOperator(
    task_id='load_cricket_data_to_gcs',
    python_callable=generate_csv_and_load_csv_to_storage,
    op_args=[url,headers,csv_filename,bucket_name],
    dag=dag,
)

load_data_to_bigquery = PythonOperator(
    task_id='load_data_to_bigquery',
    python_callable=load_csv_to_bigquery,
    op_args=[bucket_name, file_name, dataset_id, table_id],
    dag=dag,
)


load_cricket_data_to_gcs >> load_data_to_bigquery