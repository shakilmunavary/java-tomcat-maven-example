pipeline {
    agent any

    environment {
        APPLICATION_NAME = 'myapplication'
        ENVIRONMENT = 'Dev'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        BRANCH = 'master'
        CODE_ANALYSIS_TOOL = 'Sonar'
        TARGET_ENVIRONMENT = 'AWS EC2'
        ARTIFACT_NAME = 'java-tomcat-maven-example.war'
        TOMCAT_WEBAPP_PATH = '/opt/tomcat/webapp'
    }

    stages {
        stage('Code Checkout') {
            steps {
                echo 'Checking out code from GitHub'
                git branch: "${BRANCH}", url: "${REPO_URL}"
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application using Maven'
                sh 'mvn clean package'
            }
        }

        stage('Unit Testing') {
            steps {
                echo 'Running unit tests'
                sh 'mvn test'
            }
        }

        stage('Code Quality Analysis') {
            steps {
                // Code quality analysis using Sonar
                echo 'Running Code Quality Analysis using Sonar'
                sh 'mvn sonar:sonar'
                echo 'Code Analysis done'
            }
        }

        stage('Upload Artifacts') {
            steps {
                // Uploading artifacts to Jfrog
                echo 'Uploading artifacts to Jfrog'
                sh 'curl -u <username>:<password> -T target/${ARTIFACT_NAME} <jfrog-repository-url>'
                echo 'Upload Artifacts done'
            }
        }

        stage('Deployment') {
            steps {
                echo 'Deploying application to AWS EC2'
                sh "sudo cp target/${ARTIFACT_NAME} ${TOMCAT_WEBAPP_PATH}"
            }
        }
    }
}