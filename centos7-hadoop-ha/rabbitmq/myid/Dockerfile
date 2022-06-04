ARG IMAGE
FROM $IMAGE:ha
#FROM centos7/hadoop/rabbitmq:ha

MAINTAINER Malachai <prussian1933@naver.com>

ARG MYID
RUN echo $MYID > $ZOOKEEPER_HOME/data/myid

ENTRYPOINT ["/bin/bash"]
 
