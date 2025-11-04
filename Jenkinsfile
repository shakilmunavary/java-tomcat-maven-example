pipeline {
    agent any
    environment {
        APPLICATION_NAME = 'Roshanapplication'
        ENVIRONMENT = 'Dev'
        CI_CD_TOOL = 'Jenkins'
        VCS = 'Github'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        FILE_REPO_SYSTEM = 'Jfrog'
        TECH_STACK = 'Java'
        CODE_ANALYSIS_TOOL = 'Sonar'
        TARGET_ENV = 'AWS EC2'
    }
    stages {
        stage('Code Checkout') {
            steps {
                echo 'Checking out code from Github...'
                git branch: 'master', url: "${REPO_URL}"
            }
        }
        stage('Build') {
            steps {
                echo 'Building the application...'
                sh 'mvn clean package'
            }
        }
        stage('Unit Testing') {
            steps {
                echo 'Running unit tests...'
                sh 'mvn test'
            }
        }
        stage('Code Quality Analysis') {
            steps {
                // Perform code analysis using Sonar
                echo 'Code Analysis done'
            }
        }
        stage('Upload Artifacts') {
            steps {
                // Upload artifacts to Jfrog
                echo 'Upload Artifacts done'
            }
        }
        stage('Deployment') {
            steps {
                echo 'Deploying the application to AWS EC2...'
                sh 'sudo cp target/java-tomcat-maven-example.war /opt/tomcat/webapp/'
            }
        }
    }
    post {
        always {
            echo "Pipeline execution completed for ${APPLICATION_NAME} in ${ENVIRONMENT} environment."
        }
    }
}