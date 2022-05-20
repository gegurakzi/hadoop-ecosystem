FROM centos:centos7

MAINTAINER Malachai <prussian1933@naver.com>

RUN \
    yum update -y && \
    yum install net-tools -y && \
    yum install vim-enhanced -y && \
    yum install wget -y && \
    yum install openssh-server openssh-clients openssh-askpass -y && \
    yum install java-1.8.0-openjdk-devel.x86_64 -y && \
    mkdir /opt/jdk && \
    mkdir /opt/hadoop &&\
    ln -s /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.332.b09-1.el7_9.x86_64 /opt/jdk/current

WORKDIR /opt/hadoop
RUN wget https://mirrors.sonic.net/apache/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz && \
    tar xvzf hadoop-3.3.1.tar.gz && \
    ln -s /opt/hadoop/hadoop-3.3.1 /opt/hadoop/current

ENV JAVA_HOME=/opt/jdk/current
ENV PATH=$PATH:$JAVA_HOME/bin
ENV HADOOP_HOME=/opt/hadoop/current
ENV PATH=$PATH:$HADOOP_HOME/bin
ENV PATH=$PATH:$HADOOP_HOME/sbin
ENV HADOOP_PID_DIR=/opt/hadoop/current/pids

RUN ssh-keygen -f /etc/ssh/ssh_host_rsa_key -t rsa -N "" && \
    ssh-keygen -f /etc/ssh/ssh_host_ecdsa_key -t ecdsa -N "" && \
    ssh-keygen -f /etc/ssh/ssh_host_ed25519_key -t ed25519 -N "" && \
    /usr/sbin/sshd

RUN cd $HADOOP_HOME/etc/hadoop

WORKDIR $HADOOP_HOME/etc/hadoop
RUN echo \
$'export HADOOP_PID_DIR=/opt/hadoop/current/pids \n\
export JAVA_HOME=/opt/jdk/current \n\
export HDFS_NAMENODE_USER=\"root\" \n\
export HDFS_DATANODE_USER=\"root\" \n\
export HDFS_SECONDARYNAMENODE_USER=\"root\" \n\
export YARN_RESOURCEMANAGER_USER=\"root\" \n\
export YARN_NODEMANAGER_USER=\"root\" ' >> hadoop-env.sh
COPY core-site.xml .
COPY hdfs-site.xml .
COPY yarn-site.xml .
COPY mapred-site.xml . 

ENTRYPOINT ["/bin/bash"]
 
