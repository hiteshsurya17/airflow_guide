from datetime import datetime,timedelta

from airflow.decorators import dag,task


default_args = {
    'owner' : 'Hitesh',
    'retries' : 5,
    'retry_delay' : timedelta(minutes=2)
}

@dag(
        dag_id = 'hello_world_dag_v1',
        default_args = default_args,
        start_date = datetime(2024,3,19,2),
        schedule_interval = '@daily'
)
def hello_world_etl():

    @task()
    def get_name():
        return 'Rohit'
    
    @task()
    def get_age():
        return 21
    
    @task()
    def greet(name,age):
        print(f'hello work my name is {name} , I am {age} years old!')

    name = get_name()
    age = get_age()
    greet(name=name,age=age)

greet_dag = hello_world_etl()