pipeline {
    agent any
    environment {
        APP_NAME = 'app1'
        ENV = 'Dev'
        CI_CD_TOOL = 'Jenkins'
        VERSION_CONTROL_SYSTEM = 'Github'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        FILE_REPOSITORY_SYSTEM = 'Jfrog'
        TECH_STACK = 'Java'
        CODE_ANALYSIS_TOOL = 'Sonar'
        TARGET_ENV = 'AWS EC2'
    }
    stages {
        stage('Code Checkout') {
            steps {
                git branch: 'master', url: "${REPO_URL}"
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
                // Code quality analysis steps go here, but they are commented out
                echo 'Code Analysis done'
            }
        }
        stage('Upload Artifacts') {
            steps {
                // Artifact upload steps go here, but they are commented out
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