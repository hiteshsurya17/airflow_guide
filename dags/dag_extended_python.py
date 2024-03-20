from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator 

default_args = {
    'owner':'Hitesh',
    'retries': 5,
    'retry_delay' : timedelta(minutes=2)
}

def checking_sklearn():
    import sklearn
    print(f"sklearn version is {sklearn.__version__}")

with DAG(
    dag_id = 'dag_with_extended_packages_v1',
    default_args = default_args,
    start_date = datetime(2024,3,19),
    schedule_interval = '50 12 * * wed'
) as dag:
    check_sklearn = PythonOperator(
        task_id = 'checking_sklearn',
        python_callable = checking_sklearn
    )
check_sklearn