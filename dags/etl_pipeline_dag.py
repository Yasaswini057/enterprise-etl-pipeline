"""Airflow orchestration for the existing Enterprise ETL Pipeline phases."""

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


DEFAULT_ARGS = {
    "owner": "enterprise-etl",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}


def run_extraction_phase():
    """Invoke the existing extraction orchestration without duplicating it."""
    from extract.extractor import run_extraction

    run_extraction()


def run_transformation_phase():
    """Invoke the existing transformation orchestration without duplicating it."""
    from transform.transformer import run_transformations

    run_transformations()


def run_loading_phase():
    """Invoke the existing PostgreSQL loading orchestration without duplicating it."""
    from load.loader import run_loader

    run_loader()


with DAG(
    dag_id="enterprise_etl_pipeline",
    description="Run the existing extraction, transformation, and loading phases.",
    default_args=DEFAULT_ARGS,
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["enterprise", "etl", "postgresql"],
) as dag:
    extract_task = PythonOperator(
        task_id="extract",
        python_callable=run_extraction_phase,
    )
    transform_task = PythonOperator(
        task_id="transform",
        python_callable=run_transformation_phase,
    )
    load_task = PythonOperator(
        task_id="load",
        python_callable=run_loading_phase,
    )

    extract_task >> transform_task >> load_task
