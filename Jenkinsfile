pipeline {
    agent any
    environment {
        APP_NAME = 'app'
        ENV = 'Dev'
        CI_CD_TOOL = 'Jenkins'
        VCS = 'Github'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        FILE_REPO = 'Jfrog'
        TECH_STACK = 'Java'
        CODE_ANALYSIS_TOOL = 'Sonar'
        TARGET_ENV = 'AWS EC2'
    }
    stages {
        stage('Code Checkout') {
            steps {
                git url: REPO_URL, branch: 'main'
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
                // Code analysis steps would go here
                echo 'Code Analysis done'
            }
        }
        stage('Upload Artifacts') {
            steps {
                // Artifact upload steps would go here
                echo 'Upload Artifacts done'
            }
        }
        stage('Deployment') {
            when {
                environment name: 'TARGET_ENV', value: 'AWS EC2'
            }
            steps {
                sh 'cp java-tomcat-maven-example.war /opt/tomcat/webapps/'
            }
        }
    }
}