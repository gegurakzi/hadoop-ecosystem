FROM centos7/hadoop/hive:ha

ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV YARN_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PATH=$PATH:$HADOOP_CONF_DIR

RUN mkdir /opt/spark && \
    cd /opt/spark && \
    wget https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz && \
    tar -xzf spark-3.2.1-bin-hadoop3.2.tgz && \
    ln -s /opt/spark/spark-3.2.1-bin-hadoop3.2 /opt/spark/current

ENV SPARK_HOME=/opt/spark/current
ENV PATH=$PATH:$SPARK_HOME/bin
ENV PYSPARK_PYTHON=$PYTHON_HOME

COPY spark-defaults.conf $SPARK_HOME/conf/spark-defaults.conf
COPY spark-env.sh $SPARK_HOME/conf/spark-env.sh
