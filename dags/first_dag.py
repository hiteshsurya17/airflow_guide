from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner' : 'Hitesh',
    'retries' : '5',
    'time_delay' : timedelta(minutes=2)
}

with DAG(
    dag_id = 'first_dag_v4',
    default_args = default_args,
    description = "this is the first dag.",
    start_date = datetime(2024,3,19,3),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command="echo hello world! This is the first task."
    )
    task2 = BashOperator(
        task_id = 'second_task',
        bash_command="echo hello world! This is the second task."
    )
    task3 = BashOperator(
        task_id = 'third_task',
        bash_command="echo hello world! This is the third task i will run at the same time as task 2"
    )

# task dependency method 1
# task1 >> task2
# task1 >> task3 
# task dependency method 2
# task1.set_downstream(task2) 
# task1.set_downstream(task3)
# task dependency method 3
task1 >> [task2,task3]