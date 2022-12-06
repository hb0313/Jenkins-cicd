#/bin/bash

echo 'running docker'
echo "Building docker image using shell!!!"
docker build -t app1 .
echo "Build successfull, cleaning up..."
docker image rm app1
