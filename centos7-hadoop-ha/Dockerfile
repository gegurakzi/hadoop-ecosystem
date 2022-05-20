FROM centos7/hadoop:namenode

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
$'alias zoo-start="/opt/zookeeper/current/bin/zkServer.sh start" \n\
  alias zoo-status="/opt/zookeeper/current/bin/zkServer.sh status" \n\
  alias zoo-stop="/opt/zookeeper/current/bin/zkServer.sh stop" \n\
  zoo-start' >> $HOME/.bashrc

ENTRYPOINT ["/bin/bash"]
 
