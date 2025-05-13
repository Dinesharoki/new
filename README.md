pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'thousifk/websie-demo'
        DOCKER_TAG = 'latest'
        DOCKER_CREDENTIALS_ID = '5f1faebb-1040-40c6-b323-3918715e1342'
        GIT_REPO = 'https://github.com/Thousif10/Website.git'
        GIT_BRANCH = 'main'
        //SONARQUBE_SERVER = 'MySonarQube'  // SonarQube server name from Jenkins configuration
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: "${GIT_BRANCH}", url: "${GIT_REPO}"
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
                }
            }
        }

      /*  stage('SonarQube Analysis') {
            steps {
                script {
                    // Run SonarQube scan
                    withSonarQubeEnv(SONARQUBE_SERVER) {
                        sh 'mvn clean install sonar:sonar -Dsonar.projectKey=sonarqube -Dsonar.host.url=http://localhost:9000 -Dsonar.login=sqa_86eb0296fb7108b3d2848f097506b83928c5ef8a'
                    }
                }
            }
        } */

        stage('Testing') {
            steps {
                script {
                    sh 'docker run ${DOCKER_IMAGE}'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', "${DOCKER_CREDENTIALS_ID}") {
                        sh 'docker push ${DOCKER_IMAGE}:${DOCKER_TAG}'
                    }
                }
            }
        }
    }
}
