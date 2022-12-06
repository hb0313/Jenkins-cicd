# Jenkins-cicd

## Repo used to build docker images

## How it works?

App files along with a Dockerfile can be placed in repo. Jenkins will automatically start the build when committed.
All logs will be stored in a log file post build.

NOTE: Jenkins is running on localhost and is not accessible via internet.


## Features

- Docker build pipeline
- Build logging
- Clone repo and start auto build
- Schedule building

## Jenkinsfile

Jenkins configuration for build

```sh
pipeline {
    environment {
        dockerImage = ''
    }
    agent any
        stages {
            stage('Cloning Git') {
                steps {
                    git 'https://github.com/hb0313/Jenkins-cicd.git'
                }
            }
            stage('Building image') {
                steps{
                    withEnv(['PATH+EXTRA=/usr/sbin:/usr/bin:/sbin:/bin']) {
                        sh("sh run.sh")
                    }
                }
            }
            stage('Cleaning pipeline') {
                steps{
                    withEnv(['PATH+EXTRA=/usr/sbin:/usr/bin:/sbin:/bin'])
                        sh("docker rmi git/appbuild")
                }
            }
        }
}
```
