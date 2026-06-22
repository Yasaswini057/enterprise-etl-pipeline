from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta

"""
Enterprise ETL Pipeline

Workflow:
Extract -> Transform -> Load

Author: Team 1
"""

# Default Settings
default_args = {
    "owner": "team1",
    "retries": 2,
    "retry_delay": timedelta(minutes=1)
}

# Task Functions
def extract():
    print("Extracting data from Salesforce, Stripe and Zendesk APIs...")

def transform():
    print("Transforming and cleaning data...")

def load():
    print("Loading data into SQLite database...")

# DAG Definition
with DAG(
    dag_id="enterprise_etl_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args=default_args,
    description="Enterprise ETL Pipeline using Apache Airflow"
) as dag:

    extract_task = PythonOperator(
        task_id="extract_salesforce_stripe_zendesk_data",
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id="transform_clean_data",
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id="load_data_to_sqlite",
        python_callable=load
    )

    extract_task >> transform_task >> load_task