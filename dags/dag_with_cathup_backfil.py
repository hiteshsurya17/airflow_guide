from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner' : 'Hitesh',
    'retries' : '5',
    'time_delay' : timedelta(minutes=2)
}

with DAG(
    dag_id = 'dag_witth_cathup_backfil_v4',
    default_args = default_args,
    description = "this is the first dag.",
    start_date = datetime(2024,3,10,3),
    schedule_interval='@daily',
    catchup = False
) as dag:
    task1 = BashOperator(
        task_id = 'bash_task',
        bash_command="echo hello world!"
    )
task1