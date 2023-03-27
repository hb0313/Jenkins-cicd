build:
        docker build -t flaskweb:v1 .
run:
        docker run -it -p=8080:8080 flaskweb:v1 
