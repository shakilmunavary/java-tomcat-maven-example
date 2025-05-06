groovy
pipeline {
    agent any

    environment {
        APP_NAME = 'abc'
        ENVIRONMENT = 'Dev'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example'
        FILE_REPO = 'Nexus'
        TECH_STACK = 'Java'
        TARGET_ENV = 'VM'
        ADMIN_EMAIL = 'admin@example.com'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: REPO_URL
            }
        }
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('Quality Check') {
            steps {
                sh 'sonar-scanner -Dsonar.projectKey=${APP_NAME} -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000'
            }
        }
        stage('Deploy') {
            steps {
                sh 'deploy to ${TARGET_ENV}'
            }
        }
        stage('Notification') {
            steps {
                mail to: ADMIN_EMAIL,
                     subject: "Pipeline ${APP_NAME} for ${ENVIRONMENT} is completed",
                     body: "The pipeline has been successfully executed."
            }
        }
    }

    post {
        always {
            junit '**/target/surefire-reports/TEST-*.xml'
        }
        failure {
            mail to: ADMIN_EMAIL,
                 subject: "Pipeline ${APP_NAME} for ${ENVIRONMENT} has failed",
                 body: "The pipeline has failed. Please check the logs."
        }
    }
}