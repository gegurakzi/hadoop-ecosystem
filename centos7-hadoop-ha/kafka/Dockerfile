FROM centos7/hadoop:ha

MAINTAINER Malachai <prussian1933@naver.com>

RUN mkdir /opt/kafka && \
    cd /opt/kafka && \
    wget https://archive.apache.org/dist/kafka/2.7.0/kafka_2.13-2.7.0.tgz &&\
    tar xvfz kafka_2.13-2.7.0.tgz && \
    ln -s /opt/kafka/kafka_2.13-2.7.0.tgz /opt/kafka/current

ENV KAFKA_HOME=/opt/airflow/current
ENV PATH=$PATH:$KAFKA_HOME/bin

COPY server.properties /opt/kafka/current/config 

ENTRYPOINT ["/bin/bash"]
 
