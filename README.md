# hadoop-ecosystem

Description:

Namenode: master01, master02
Datanode: slave01, slave02, slave03
Jouralnode: master01, master02, slave01
Hive: master01, master02
Spark: master01, master02
Airflow(celery workers): master01, master02, slave01(with webserver, scheduler), slave02, slave03
Flume: slave03

Namenode Web: 50070(master01) 50071(master02)
Node Manager Web: 8042(master01) 8043(master02)
Resource Manager Web: 8088(master01) 8089(master02)
MapReduce JobHistory Web: 19888(master01) 19889(master02)
Spark Application Manager Web(4040 4041 -> redirect to YARN Resource Manager/Spark Application): 8088/app_id#(master01) 8089/app_id#(master02)
Spark History Web: 18080(master01) 18081(master02)
Airflow WebServer: 5082(default: 8080)
RabbitMQ Server: 15672
Flower UI(web management for Airflow celery workers): 5555

[slave01 ~]$ rabbitmq-plugins enable rabbitmq_management
[slave01 ~]$ /sbin/rabbitmq-server -detached

// if not initialized
[slave01 ~]$ airflow db init

[slave01 ~]$ airflow webserver -D &
[slave01 ~]$ airflow scheduler -D &
[slave01 ~]$ airflow celery flower -D &
[slave01 ~]$ airflow celery worker -D -q queue-slave01 &
[master01 ~]$ airflow celery worker -D -q queue-master01 &
[master02 ~]$ airflow celery worker -D -q queue-master02 &
[slave02 ~]$ airflow celery worker -D -q queue-slave02 &
[slave03 ~]$ airflow celery worker -D -q queue-slave03 &

// if not created
[slave01 ~]$ airflow users create
--username guest
--firstname aa
--lastname bb
--role Admin
--email xx@xx.com

[master01 ~]$ $HADOOP_HOME/bin/hdfs zkfc -formatZK
[master01 ~]$ $HADOOP_HOME/bin/hdfs --daemon start journalnode
[master01 ~]$ start-all.sh ---> most effient way to initialize SSH connections
[master01 ~]$ hdfs namenode -format
[master01 ~]$ $HADOOP_HOME/bin/hdfs --daemon start namenode
[master02 ~]$ hdfs namenode -bootstrapStandby
[masterp02 ~]$ $HADOOP_HOME/bin/hdfs --daemon start namenode
[slave01 ~]$ $HADOOP_HOME/bin/hdfs --daemon start datanode
[slave02 ~]$ $HADOOP_HOME/bin/hdfs --daemon start datanode
[slave03 ~]$ $HADOOP_HOME/bin/hdfs --daemon start datanode
[master01 ~]$ start-yarn.sh
[master01 ~]$ $HADOOP_HOME/bin/mapred --daemon start historyserver
[master02 ~]$ $HADOOP_HOME/bin/mapred --daemon start historyserver

hive:
[master01 ~]$ hive

spark:
[master01 ~]$ hdfs dfs -mkdir /user
[master01 ~]$ hdfs dfs -mkdir /user/hadoop
[master01 ~]$ hdfs dfs -mkdir /user/hadoop/sparklog
[master01 ~]$ pyspark
[master01 ~]$ $SPARK_HOME/sbin/start-history-server.sh

Flume: 
[slave03 ~]$ flume-ng agent -n agent1 -c $FLUME_HOME/conf -f $FLUME_HOME/conf/flume-conf.properties -Dflume.log.dir=$FLUME_HOME/log
