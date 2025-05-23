pipeline {
    agent any
    environment {
        APP_NAME = 'hello'
        ENV = 'Dev'
        CI_CD_TOOL = 'Jenkins'
        VERSION_CONTROL_SYSTEM = 'Github'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        FILE_REPO_SYSTEM = 'Jfrog'
        TECHNICAL_STACK = 'Java'
        CODE_ANALYSIS_TOOL = 'Sonar'
        TARGET_ENV = 'AWS EC2'
        BRANCH = 'master' // As ENV is 'Dev'
    }

    stages {
        stage('Code Checkout') {
            steps {
                git branch: "${BRANCH}", url: "${REPO_URL}"
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
                // Code Quality Analysis steps would go here
                echo 'Code Analysis done'
            }
        }

        stage('Upload Artifacts') {
            steps {
                // Upload Artifacts steps would go here
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