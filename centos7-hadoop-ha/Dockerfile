FROM centos7/hadoop:nn

MAINTAINER Malachai <prussian1933@naver.com>

RUN mkdir /opt/zookeeper && \
    cd /opt/zookeeper && \
    wget https://mirror.navercorp.com/apache/zookeeper/zookeeper-3.6.3/apache-zookeeper-3.6.3-bin.tar.gz &&\
    tar xvfz apache-zookeeper-3.6.3-bin.tar.gz && \
    ln -s /opt/zookeeper/apache-zookeeper-3.6.3-bin /opt/zookeeper/current && \
    mkdir current/data

ENV ZOOKEEPER_HOME=/opt/zookeeper/current
ENV PATH=$PATH:$ZOOKEEPER_HOME/bin

COPY zoo.cfg /opt/zookeeper/current/conf 
COPY core-site.xml $HADOOP_HOME/etc/hadoop
COPY hdfs-site.xml $HADOOP_HOME/etc/hadoop
COPY yarn-site.xml $HADOOP_HOME/etc/hadoop
COPY mapred-site.xml $HADOOP_HOME/etc/hadoop 

RUN echo \
$'export HDFS_JOURNALNODE_USER=\"root\" \n\
  export HDFS_ZKFC_USER=\"root\" \n\
  export YARN_PROXYSERVER_USER=\"root\" ' >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh && \
   echo \
$'JAVA_HEAP_MAX=Xmx1024m' >> $HADOOP_HOME/etc/hadoop/yarn-env.sh && \
   echo \
$'alias zoo-start="/opt/zookeeper/current/bin/zkServer.sh start" \n\
  alias zoo-status="/opt/zookeeper/current/bin/zkServer.sh status" \n\
  alias zoo-stop="/opt/zookeeper/current/bin/zkServer.sh stop" \n\
  zoo-start' >> $HOME/.bashrc

ENV AIRFLOW_HOME=/opt/airflow/current

RUN AIRFLOW_VERSION=2.0.0 && \
    PYTHON_VERSION=3.6 && \
    mkdir /opt/airflow && \
    mkdir /opt/airflow/airflow-${AIRFLOW_VERSION} && \
    mkdir /opt/airflow/airflow-${AIRFLOW_VERSION}/dags && \
    mkdir /opt/airflow/airflow-${AIRFLOW_VERSION}/logs && \
    ln -s /opt/airflow/airflow-${AIRFLOW_VERSION} /opt/airflow/current && \
    cd /opt/airflow && \
    pip3 install --upgrade pip && \
    pip install --upgrade setuptools &&\
    pip install -U pip setuptools wheel && \
    export SLUGIFY_USES_TEXT_UNIDECODE=yes && \
    yum -y install epel-release gcc gcc-c++ glibc-core glibc-common mysql-devel python-devel python-setuptools python3-devel python3-pip openldap-devel && \
    pip install pytz pyOpenSSL ndg-httpsclient mysqlclient celery flower apache-airflow==${AIRFLOW_VERSION} \
                        --constraint https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt

COPY airflow.cfg $AIRFLOW_HOME

ENTRYPOINT ["/bin/bash"]
 
