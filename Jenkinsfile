pipeline {
    agent any
    environment {
        APP_NAME = 'Application'
        ENVIRONMENT = 'Dev'
        CI_CD_TOOL = 'Jenkins'
        VERSION_CONTROL = 'Github'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        FILE_REPO = 'Jfrog'
        TECH_STACK = 'Java'
        CODE_ANALYSIS_TOOL = 'Sonar'
        TARGET_ENV = 'AWS EC2'
    }
    stages {
        stage('Code Checkout') {
            steps {
                git branch: 'master', url: REPO_URL
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
                // Code analysis tool commands here
                echo 'Code Analysis done'
            }
        }
        stage('Upload Artifacts') {
            steps {
                // File repository commands here
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