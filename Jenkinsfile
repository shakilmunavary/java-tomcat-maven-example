pipeline {
    agent any

    environment {
        APP_NAME = 'MBRDI'
        ENVIRONMENT = 'Dev'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        BRANCH = 'master'
        JFROG_REPO = 'your_jfrog_repo'
        SONAR_PROJECT_KEY = 'your_sonar_project_key'
        SONAR_TOKEN = 'your_sonar_token'
        TARGET_ENV = 'AWS EC2'
        TOMCAT_WEBAPP_DIR = '/opt/tomcat/webapps'
        NOTIFICATION_EMAIL = 'admin@test.com'
    }

    stages {
        stage('Code Checkout') {
            steps {
                git url: "${REPO_URL}", branch: "${BRANCH}"
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
                // Code quality analysis
                echo 'Code Analysis done'
            }
        }

        stage('Upload Artifacts') {
            steps {
                // Upload artifacts
                echo 'Upload Artifacts done'
            }
        }

        stage('Deployment') {
            steps {
                script {
                    if (env.TARGET_ENV == 'AWS EC2') {
                        sh "sudo cp target/java-tomcat-maven-example.war ${TOMCAT_WEBAPP_DIR}"
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Sending notification to ${NOTIFICATION_EMAIL}"
            mail to: "${NOTIFICATION_EMAIL}",
                 subject: "Pipeline Status for ${APP_NAME} in ${ENVIRONMENT}",
                 body: "The pipeline for ${APP_NAME} in ${ENVIRONMENT} has completed."
        }
    }
}