pipeline {
    agent any

    environment {
        APP_NAME = 'Test'
        ENVIRONMENT = 'Dev'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        BRANCH_NAME = 'master'
        TARGET_ENV = 'AWS ECS'
    }

    stages {
        stage('Code Checkout') {
            steps {
                git url: "${REPO_URL}", branch: "${BRANCH_NAME}"
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
                // Code quality analysis using Sonar
                sh 'mvn sonar:sonar'
                echo 'Code Analysis done'
            }
        }

        stage('Upload Artifacts') {
            steps {
                // Upload artifacts to Nexus
                sh 'mvn deploy'
                echo 'Upload Artifacts done'
            }
        }

        stage('Deployment') {
            steps {
                script {
                    if (env.TARGET_ENV == 'AWS ECS') {
                        // Deployment steps for AWS ECS
                        sh 'echo Deploying to AWS ECS'
                    } else if (env.TARGET_ENV == 'AWS EC2') {
                        // Deployment steps for AWS EC2
                        sh 'sudo cp target/java-tomcat-maven-example.war /opt/tomcat/webapps/'
                    }
                }
            }
        }
    }
}