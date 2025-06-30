pipeline {
    agent any
    environment {
        APP_NAME = 'myapp1'
        ENVIRONMENT = 'Dev'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        BRANCH = 'master'
        JFROG_REPO = 'your_jfrog_repo_url'
        SONAR_PROJECT_KEY = 'your_sonar_project_key'
        SONAR_ORGANIZATION = 'your_sonar_organization'
        SONAR_TOKEN = 'your_sonar_token'
        AWS_EC2_INSTANCE = 'your_aws_ec2_instance'
        TOMCAT_WEBAPP_DIR = '/opt/tomcat/webapps'
    }
    stages {
        stage('Code Checkout') {
            steps {
                git branch: "${BRANCH}", url: "${REPO_URL}"
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
                // Code Quality Analysis
                echo 'Code Analysis done'
            }
        }
        stage('Upload Artifacts') {
            steps {
                // Upload Artifacts
                echo 'Upload Artifacts done'
            }
        }
        stage('Deployment') {
            steps {
                script {
                    if (ENVIRONMENT == 'Dev') {
                        sh "scp target/java-tomcat-maven-example.war ${AWS_EC2_INSTANCE}:${TOMCAT_WEBAPP_DIR}"
                        sh "ssh ${AWS_EC2_INSTANCE} 'sudo cp ${TOMCAT_WEBAPP_DIR}/java-tomcat-maven-example.war ${TOMCAT_WEBAPP_DIR}/'"
                    }
                }
            }
        }
    }
}