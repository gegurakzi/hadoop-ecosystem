ARG IMAGE
FROM $IMAGE

MAINTAINER Malachai <prussian1933@naver.com>

ARG MYID
RUN echo $MYID > $ZOOKEEPER_HOME/data/myid

RUN mkdir /opt/kafka && \
    cd /opt/kafka && \
    wget https://archive.apache.org/dist/kafka/2.7.0/kafka_2.13-2.7.0.tgz &&\
    tar xvfz kafka_2.13-2.7.0.tgz && \
    ln -s /opt/kafka/kafka_2.13-2.7.0 /opt/kafka/current

ENV KAFKA_HOME=/opt/kafka/current
ENV PATH=$PATH:$KAFKA_HOME/bin

COPY server${MYID}.properties /opt/kafka/current/config/server.properties

ENTRYPOINT ["/bin/bash"]

