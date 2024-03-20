from datetime import datetime,timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args ={
    'owner' : 'Hitesh',
    'retries' : 5,
    'retry_delay' : timedelta(seconds=2)
}

with DAG(
    dag_id = 'dag_with_cron_expression_v4',
    default_args = default_args,
    start_date = datetime(2024,3,10,2),
    schedule_interval = '5 4 * * tue-thu'
) as dag:
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command="echo I run this task at every tue, wednesday and thursday on 4:05 am, you can look up the cron expression on crontab guru!"
    )
task1