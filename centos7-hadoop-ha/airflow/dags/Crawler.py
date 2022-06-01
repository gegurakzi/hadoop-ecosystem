import os
import sys
sys.path.append(os.path.dirname('/opt/airflow/current/dags/pyscripts/yfinance'))
#os.environ['PATH'] += os.pathsep + '/opt/airflow/current/dags/pyscripts'

from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from textwrap import dedent
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from pyscripts.YFinanceTickerWriter import ticker_tofiles


default_args = {
    'start_date': days_ago(1),
}

dag = DAG(
    'YFinance_Crawler_DAG',
    default_args=default_args,
    schedule_interval='@once'
)

t1 = PythonOperator(
    task_id='AAPL2files',
	provide_context=True,
    python_callable=ticker_tofiles,
	op_kwargs={'ticker': 'AAPL',
		      'outdir': '/opt/flume/current/source1_workdir/'},
    queue='queue-slave03',
    dag=dag
)

t1
