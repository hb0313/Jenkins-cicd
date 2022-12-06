#/bin/bash

echo 'running docker'
docker build -t app1 .
docker rm image app1
