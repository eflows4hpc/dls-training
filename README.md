# dls-training
Materials for internal DLS training

## Setup

```
python3 -m venv .
source bin/activate
python3 -m pip install apache-airflow
airflow standalone
```

Check `~/airflow/airflow.cfg` to find out where the airflow expects dags to be present, and change it to current folder

``
     dags_folder = ~/airflow/dags
``

Go to http://localhost:8080 password to login is in the console or `cat ~/airflow/standalone_admin_password.txt`

