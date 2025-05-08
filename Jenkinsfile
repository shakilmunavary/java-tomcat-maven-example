pipeline {
    agent any
    environment {
        APP_NAME = 'app'
        ENV = 'Dev'
        CI_CD_TOOL = 'Jenkins'
        VCS = 'Github'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        ARTIFACTS_REPO = 'Jfrog'
        TECH_STACK = 'Java'
        CODE_ANALYSIS_TOOL = 'Sonar'
        TARGET_ENV = 'AWS EC2'
        BRANCH = 'master'
    }
    stages {
        stage('Code Checkout') {
            steps {
                git branch: BRANCH, url: REPO_URL
            }
        }
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('Unit Testing') {
            steps {
                sh 'mvn test'
            }
        }
        stage('Code Quality Analysis') {
            steps {
                // Code analysis tool steps go here
                echo 'Code Analysis done'
            }
        }
        stage('Upload Artifacts') {
            steps {
                // Artifacts repository upload steps go here
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