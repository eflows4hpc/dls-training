from airflow.contrib.sensors.python_sensor import PythonSensor
from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

import random

default_args = {
    'owner': 'airflow',
}


def my_func():
   return random.choice(10*[False]+[True])
    

@dag(default_args=default_args, schedule_interval=None, start_date=days_ago(2), tags=['example'])
def sensor_example():

    @task
    def doint_noting():
        print("I am not doing anything")
        return 1
    
    sensor = PythonSensor(python_callable=my_func, task_id='cleanup')

    res = doint_noting()
    sensor >> res
    
dag = sensor_example()
