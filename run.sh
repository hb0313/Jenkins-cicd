#/bin/bash

exec > log.txt 2>&1

docker build -t git/appbuild .
