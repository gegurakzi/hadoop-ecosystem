from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from textwrap import dedent
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'start_date': days_ago(1),
}

dag = DAG(
    'FlumeDAG_test',
    default_args=default_args,
    schedule_interval='@once'
)

t1 = BashOperator(
    task_id='echo1',
    bash_command='echo -e "This is First test file generation" > /opt/flume/current/source1_workdir/.file1.txt',
    queue='queue-slave03',
    dag=dag
)

t2 = BashOperator(
    task_id='sleep1',
    bash_command='sleep 1',
    queue='queue-slave03',
    dag=dag
)

t3 = BashOperator(
    task_id='mv1',
    bash_command='mv /opt/flume/current/source1_workdir/.file1.txt /opt/flume/current/source1_workdir/file1.txt',
    queue='queue-slave03',
    dag=dag
)

t4 = BashOperator(
    task_id='echo2',
    bash_command='echo -e "This is Second test file generation" > /opt/flume/current/source1_workdir/.file2.txt',
    queue='queue-slave03',
    dag=dag
)

t5 = BashOperator(
    task_id='sleep2',
    bash_command='sleep 1',
    queue='queue-slave03',
    dag=dag
)

t6 = BashOperator(
    task_id='mv2',
    bash_command='mv /opt/flume/current/source1_workdir/.file2.txt /opt/flume/current/source1_workdir/file2.txt',
    queue='queue-slave03',
    dag=dag
)


t1 >> t2 >> t3 >> t4 >> t5 >> t6
