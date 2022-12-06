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
                    withEnv(['PATH+EXTRA=/usr/sbin:/usr/bin:/sbin:/bin']) {
                        sh("docker rmi git/appbuild")
                    }
                }
            }
        }
}