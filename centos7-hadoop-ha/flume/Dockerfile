FROM centos7/hadoop:ha

MAINTAINER Malachai <prussian1933@naver.com>

RUN mkdir /opt/flume && \
    cd /opt/flume && \
    wget https://dlcdn.apache.org/flume/1.9.0/apache-flume-1.9.0-bin.tar.gz &&\
    tar xvfz apache-flume-1.9.0-bin.tar.gz && \
    ln -s /opt/flume/apache-flume-1.9.0-bin /opt/flume/current && \
    mkdir /opt/flume/current/source1_workdir

ENV FLUME_HOME=/opt/flume/current
ENV PATH=$PATH:$FLUME_HOME/bin

COPY flume-conf.properties /opt/flume/current/conf

ENTRYPOINT ["/bin/bash"]
 
