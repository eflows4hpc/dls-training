import os
import requests

from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'airflow',
}


@dag(default_args=default_args, schedule_interval=None, start_date=days_ago(2), tags=['example'])
def myfirstdag():
    
    @task
    def generate_names():
        return ['/tmp/a.txt', '/tmp/b.txt']

    @task
    def process_files(files):
        for fname in files:
            print(f"Processing file {fname}")

dag = myfirstdag()
