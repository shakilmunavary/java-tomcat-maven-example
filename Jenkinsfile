pipeline {
    agent any
    environment {
        APP_NAME = "Roshan"
        ENV = "Dev"
        REPO_URL = "https://github.com/shakilmunavary/java-tomcat-maven-example.git"
        FILE_REPO = "Jfrog"
        TECH_STACK = "Java"
        QUALITY_TOOL = "Sonar"
        TARGET_ENV = "VM"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: "${REPO_URL}"
            }
        }
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }
        stage('Quality Check') {
            steps {
                sh 'mvn sonar:sonar'
            }
        }
        stage('Deploy') {
            steps {
                sh 'jfrog rt upload "target/*.war" "${FILE_REPO}/${APP_NAME}/${ENV}/"'
            }
        }
        stage('Notification') {
            steps {
                sh 'echo "Pipeline completed. Check deployment on ${TARGET_ENV}." | mail -s "${APP_NAME} Pipeline Notification" email@example.com'
            }
        }
    }
}
