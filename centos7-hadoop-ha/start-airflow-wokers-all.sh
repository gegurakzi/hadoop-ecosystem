#!bin/bash

docker exec slave01 airflow celery worker -D -q queue-slave01 &
docker exec master01 airflow celery worker -D -q queue-master01 &
docker exec master02 airflow celery worker -D -q queue-master02 &
docker exec slave02 airflow celery worker -D -q queue-slave02 &
docker exec slave03 airflow celery worker -D -q queue-slave03 &
