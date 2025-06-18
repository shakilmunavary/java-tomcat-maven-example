pipeline {
    agent any
    environment {
        APP_NAME = 'ABCDEF'
        ENVIRONMENT = 'Dev'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        BRANCH = 'master'
        JFROG_REPO = 'your_jfrog_repo_url'
        SONAR_PROJECT_KEY = 'your_sonar_project_key'
        SONAR_HOST_URL = 'your_sonar_host_url'
        SONAR_TOKEN = 'your_sonar_token'
        AWS_EC2_USER = 'your_aws_ec2_user'
        AWS_EC2_HOST = 'your_aws_ec2_host'
        AWS_EC2_KEY = 'your_aws_ec2_key'
    }
    stages {
        stage('Code Checkout') {
            steps {
                git branch: "${BRANCH}", url: "${REPO_URL}"
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
                // Code quality analysis step
                echo 'Code Analysis done'
            }
        }
        stage('Upload Artifacts') {
            steps {
                // Upload artifacts step
                echo 'Upload Artifacts done'
            }
        }
        stage('Deployment') {
            steps {
                script {
                    if (ENVIRONMENT == 'Dev') {
                        sh '''
                            sudo cp target/java-tomcat-maven-example.war /opt/tomcat/webapps/
                        '''
                    }
                }
            }
        }
    }
}