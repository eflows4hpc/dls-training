# dls-training
Materials for internal DLS training

## Setup

python3 -m venv .
source bin/activate
python3 -m pip install apache-airflow
airflow standalone

(check ~/airflow/airflow.cfg
     dags_folder = ~/airflow/dags
)
http://localhost:8080 password to login is in the console or cat ~/airflow/standalone_admin_password.txt

