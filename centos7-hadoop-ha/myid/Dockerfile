FROM centos7/hadoop/zookeeper:node

MAINTAINER Malachai <prussian1933@naver.com>

ARG MYID
RUN echo $MYID > $ZOOKEEPER_HOME/data/myid

ENTRYPOINT ["/bin/bash"]
 
