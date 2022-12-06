#/bin/bash

exec > log.txt 2>&1

docker build -t git/appbuild .

cat log.txt

git add log.txt

git commit -m 'logs added'

git push -u origin master
