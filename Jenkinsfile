pipeline {
    agent any
    environment {
        APP_NAME = 'Testing'
        ENVIRONMENT = 'Dev'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        BRANCH = 'master'
        TARGET_ENV = 'AWS ECS'
        ADDITIONAL_INPUTS = 'Testing Purpose'
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
                    if (env.TARGET_ENV == 'AWS ECS') {
                        // Deployment steps for AWS ECS
                    } else if (env.TARGET_ENV == 'AWS EC2') {
                        sh 'sudo cp target/java-tomcat-maven-example.war /opt/tomcat/webapps/'
                    }
                }
            }
        }
    }
}