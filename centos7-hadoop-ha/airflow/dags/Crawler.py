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

outdir = '/opt/airflow/current/output'
hdfsdir = '/user/hadoop/airflow'

ticker_list = ['AAPL', 'MSFT']

t1 = []
for ticker in ticker_list:
    t1.append(PythonOperator(
        task_id=ticker+'2files',
	    provide_context=True,
        python_callable=ticker_tofiles,
	    op_kwargs={'ticker': ticker,
		       'outdir': outdir},
        queue='queue-slave03',
        dag=dag
    ))


t2 = BashOperator(
    task_id='CopyFromLocal',
    bash_command="hdfs dfs -put -t 4 "+outdir+" "+hdfsdir,
    queue='queue-slave03',
    dag=dag
)

t3 = BashOperator(
    task_id='ClearOutDIr',
    bash_command='rm -f '+outdir+'/*', 
    queue='queue-slave03',
    dag=dag
)

t1 >> t2 >> t3
