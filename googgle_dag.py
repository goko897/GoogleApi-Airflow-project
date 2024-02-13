from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.date import days_ago
from datetime import datetime
from google_etl import run_google_etl
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['airflow@example.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}
dag=DAG(
    'google_dag',
    default_args=default_args,
    description='A simple tutorial DAG',
    
)
run_etl= PythonOperator(
    task_id='complete_google_etl',
    python_callable=run_google_etl,
    dag=dag,
)
run_etl