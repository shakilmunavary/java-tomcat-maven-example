pipeline {
    agent any
    environment {
        APPLICATION_NAME = 'Firstapplication'
        ENVIRONMENT = 'Dev'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        TARGET_ENV = 'AWS EC2'
    }
    stages {
        stage('Code Checkout') {
            steps {
                echo 'Checking out code from GitHub repository...'
                git branch: 'master', url: "${REPO_URL}"
            }
        }
        stage('Build') {
            steps {
                echo 'Building the application...'
                sh 'mvn clean package'
            }
        }
        stage('Unit Testing') {
            steps {
                echo 'Running unit tests...'
                sh 'mvn test'
            }
        }
        stage('Code Quality Analysis') {
            steps {
                echo 'Performing code quality analysis...'
                // Run SonarQube analysis here
                echo 'Code Analysis done'
            }
        }
        stage('Upload Artifacts') {
            steps {
                echo 'Uploading artifacts to Jfrog...'
                // Add Jfrog CLI commands to upload artifacts
                echo 'Upload Artifacts done'
            }
        }
        stage('Deployment') {
            steps {
                script {
                    if ("${TARGET_ENV}" == 'AWS EC2') {
                        echo 'Deploying application to AWS EC2...'
                        sh 'sudo cp target/java-tomcat-maven-example.war /opt/tomcat/webapp/'
                    }
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}