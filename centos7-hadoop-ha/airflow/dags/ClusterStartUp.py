from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from textwrap import dedent
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.trigger_rule import TriggerRule

default_args = {
    'start_date': days_ago(1),
}

dag = DAG(
    'ClusterStartUp',
    default_args=default_args,
    schedule_interval='@once'
)

master01_t1 = BashOperator(
    task_id='zkformat01',
    bash_command='$HADOOP_HOME/bin/hdfs zkfc -formatZK',
    depends_on_past=True,
    trigger_rule=TriggerRule.ALL_DONE,
    queue='queue-master01',
    dag=dag
)

master01_t2 = BashOperator(
    task_id='jnstart01',
    bash_command='$HADOOP_HOME/bin/hdfs --daemon start journalnode',
    depends_on_past=True,
    trigger_rule=TriggerRule.ALL_DONE,
    queue='queue-master01',
    dag=dag
)

master01_t3 = BashOperator(
    task_id='startall01',
    bash_command='start-all.sh',
    depends_on_past=True,
    trigger_rule=TriggerRule.ALL_DONE,
    queue='queue-master01',
    dag=dag
)

master01_t4 = BashOperator(
    task_id='hdfsformat01',
    bash_command='hdfs namenode -format',
    depends_on_past=True,
    trigger_rule=TriggerRule.ALL_DONE,
    queue='queue-master01',
    dag=dag
)

master01_t5 = BashOperator(
    task_id='nnstart01',
    bash_command='$HADOOP_HOME/bin/hdfs --daemon start namenode',
    depends_on_past=True,
    trigger_rule=TriggerRule.ALL_DONE,
    queue='queue-master01',
    dag=dag
)

master02_t1 = BashOperator(
    task_id='nnbootstrap02',
    bash_command='hdfs namenode -bootstrapStandby',
    depends_on_past=True,
    trigger_rule=TriggerRule.ALL_DONE,
    queue='queue-master02',
    dag=dag
)

master02_t2 = BashOperator(
    task_id='nnstart02',
    bash_command='$HADOOP_HOME/bin/hdfs --daemon start namenode',
    depends_on_past=True,
    trigger_rule=TriggerRule.ALL_DONE,
    queue='queue-master02',
    dag=dag
)

slave01_t1 = BashOperator(
    task_id='dnstarts01',
    bash_command='$HADOOP_HOME/bin/hdfs --daemon start datanode',
    depends_on_past=True,
    trigger_rule=TriggerRule.ALL_DONE,
    queue='queue-slave01',
    dag=dag
)

slave02_t1 = BashOperator(
    task_id='dnstarts02',
    bash_command='$HADOOP_HOME/bin/hdfs --daemon start datanode',
    depends_on_past=True,
    trigger_rule=TriggerRule.ALL_DONE,
    queue='queue-slave02',
    dag=dag
)

slave03_t1 = BashOperator(
    task_id='dnstarts03',
    bash_command='$HADOOP_HOME/bin/hdfs --daemon start datanode',
    depends_on_past=True,
    trigger_rule=TriggerRule.ALL_DONE,
    queue='queue-slave03',
    dag=dag
)

master01_t6 = BashOperator(
    task_id='startyarn01',
    bash_command='start-yarn.sh',
    depends_on_past=True,
    trigger_rule=TriggerRule.ALL_DONE,
    queue='queue-master01',
    dag=dag
)

master01_t7 = BashOperator(
    task_id='hsstart01',
    bash_command='$HADOOP_HOME/bin/mapred --daemon start historyserver',
    depends_on_past=True,
    trigger_rule=TriggerRule.ALL_DONE,
    queue='queue-master01',
    dag=dag
)

master02_t3 = BashOperator(
    task_id='hsstart02',
    bash_command='$HADOOP_HOME/bin/mapred --daemon start historyserver',
    depends_on_past=True,
    trigger_rule=TriggerRule.ALL_DONE,
    queue='queue-master02',
    dag=dag
)


master01_t1 >> master01_t2 >> master01_t3 >> master01_t4 >> master01_t5 >> master02_t1 >> master02_t2 >> slave01_t1 >> slave02_t1 >> slave03_t1 >> master01_t6 >> master01_t7 >> master02_t3


