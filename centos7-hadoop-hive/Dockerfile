FROM centos:hadoop

RUN mkdir /opt/hive

WORKDIR /opt/hive
RUN wget https://dlcdn.apache.org/hive/hive-3.1.3/apache-hive-3.1.3-bin.tar.gz && \
    tar -xzvf apache-hive-3.1.3-bin.tar.gz && \
    ln -s /opt/hive/apache-hive-3.1.3-bin /opt/hive/current

ENV HIVE_HOME=/opt/hive/current
ENV PATH=$PATH:$HIVE_HOME/bin

RUN wget https://downloads.mysql.com/archives/get/p/3/file/mysql-connector-java-8.0.28.tar.gz && \
    tar -zxvf mysql-connector-java-8.0.28.tar.gz && \
    mv mysql-connector-java-8.0.28/mysql-connector-java-8.0.28.jar $HIVE_HOME/lib
COPY hive-site.xml $HIVE_HOME/conf

ENTRYPOINT ["/bin/bash"]
