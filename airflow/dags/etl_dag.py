from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Task Functions
def extract():
    print("Extracting data from APIs...")

def transform():
    print("Transforming data...")

def load():
    print("Loading data into PostgreSQL...")

# DAG Definition
with DAG(
    dag_id="enterprise_etl_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id="load_data",
        python_callable=load
    )

    