pipeline {
    agent any
    environment {
        APP_NAME = 'ABC'
        ENVIRONMENT = 'Dev'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example'
        FILE_REPO = 'Jfrog'
        TECH_STACK = 'Java'
        QUALITY_TOOLS = 'Sonar'
        TARGET_ENV = 'VM'
    }
    stages {
        stage('Checkout') {
            steps {
                git url: REPO_URL
            }
        }
        stage('Build') {
            steps {
                sh 'mvn clean install'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                script {
                    def sonarQubeScannerHome = tool 'SonarQubeScanner'
                    withSonarQubeEnv('SonarQube') {
                        sh "${sonarQubeScannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'mvn deploy'
            }
        }
    }
    post {
        failure {
            mail to: 'admin@test.com',
                 subject: "Jenkins: ${APP_NAME} - Build Failed",
                 body: "The build of ${APP_NAME} has failed. Please check the logs."
        }
    }
}