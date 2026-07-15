from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
default_args = {
    "owner": "himanshu",
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}
def greet():
    print("Hello from a PythonOperator task running inside the DAG")
with DAG(
    dag_id="hello_composer",
    description="A minimal DAG to verify the environment",
    default_args=default_args,
    schedule_interval="@daily", # runs once a day
    start_date=datetime(2026, 7, 1),
    catchup=False, # don't backfill past runs
    tags=["training", "demo"],
) as dag:
 task_start = BashOperator(
 task_id="say_hello_bash",
 bash_command="echo 'Starting the pipeline...'",
 )
 task_python = PythonOperator(
 task_id="say_hello_python",
 python_callable=greet,
 )
 task_end = BashOperator(
 task_id="say_done",
 bash_command="echo 'Pipeline complete.'",
 )
 # Define the order of execution
 task_start >> task_python >> task_end
