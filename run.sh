#/bin/bash

exec > log.txt 2>&1

docker build -t git/appbuild .

git add log.txt

git commit -m 'logs added'

git push -u origin master
