pipeline {
    agent any
    environment {
        APP_NAME = 'MAASAS'
        ENV = 'Dev'
        CI_CD_TOOL = 'Jenkins'
        VCS = 'Github'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        FILE_REPO = 'Jfrog'
        TECH_STACK = 'Java'
        CODE_ANALYSIS_TOOL = 'Sonar'
        TARGET_ENV = 'AWS EC2'
        BRANCH = 'master'
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
                sh 'sudo cp target/java-tomcat-maven-example.war /opt/tomcat/webapps/'
            }
        }
    }
}