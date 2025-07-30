pipeline {
    agent any
    environment {
        APP_NAME = 'Sanofi'
        ENVIRONMENT = 'Dev'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        BRANCH = 'master'
        JFROG_URL = 'https://your-jfrog-url.com'
        SONAR_URL = 'https://your-sonar-url.com'
        AWS_EC2_INSTANCE = 'your-ec2-instance'
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
                    if (env.ENVIRONMENT == 'Dev') {
                        sh 'sudo cp target/java-tomcat-maven-example.war /opt/tomcat/webapps/'
                    }
                }
            }
        }
    }
}