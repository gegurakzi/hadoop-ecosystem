from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from textwrap import dedent
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'start_date': days_ago(1),
}

dag = DAG(
    'ClusterDAG_test',
    default_args=default_args,
    schedule_interval='@once'
)

t1 = BashOperator(
    task_id='t1',
    bash_command='sleep 1',
    queue='queue-slave01',
    dag=dag
)

t2 = BashOperator(
    task_id='t2',
    bash_command='sleep 1',
    queue='queue-slave02',
    dag=dag
)

t3 = BashOperator(
    task_id='t3',
    bash_command='sleep 1',
    queue='queue-master01',
    dag=dag
)

t1 >> [t2, t3]
