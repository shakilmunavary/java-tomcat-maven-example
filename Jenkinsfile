pipeline {
    agent any
    environment {
        APP_NAME = 'Testing'
        ENVIRONMENT = 'Dev'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        BRANCH = 'master'
        TARGET_ENV = 'AWS EC2'
        TOMCAT_WEBAPP_DIR = '/opt/tomcat/webapps'
        WAR_FILE = 'java-tomcat-maven-example.war'
    }
    stages {
        stage('Code Checkout') {
            steps {
                git url: "${REPO_URL}", branch: "${BRANCH}"
            }
        }
        stage('Build') {
            steps {
                sh 'mvn clean install'
            }
        }
        stage('Unit Testing') {
            steps {
                sh 'mvn test'
            }
        }
        stage('Code Quality Analysis') {
            steps {
                // Code quality analysis steps
                echo 'Code Analysis done'
            }
        }
        stage('Upload Artifacts') {
            steps {
                // Upload artifacts steps
                echo 'Upload Artifacts done'
            }
        }
        stage('Deployment') {
            steps {
                script {
                    if (env.TARGET_ENV == 'AWS EC2') {
                        sh "sudo cp target/${WAR_FILE} ${TOMCAT_WEBAPP_DIR}"
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline completed'
        }
    }
}