from datetime import datetime,timedelta
from airflow import DAG 
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

default_args = {
    'owner': 'Hitesh',
    'retry': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id = 'dag_sensor_minio_s3_v5',
    default_args = default_args,
    start_date = datetime(2024,3,19),
    schedule_interval = '3 4 * * *'
) as dag:
    minio_task = S3KeySensor(
        task_id = 'sensing_s3',
        aws_conn_id = 'minio_s3',
        bucket_key = 'data.csv',
        bucket_name = 'airflow',
        mode = 'poke',
        poke_interval =5,
        timeout = 30
    )

minio_task