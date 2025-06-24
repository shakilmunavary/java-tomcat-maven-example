pipeline {
    agent any

    environment {
        APP_NAME = 'LMNOP'
        ENVIRONMENT = 'Dev'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        BRANCH = 'master'
        JFROG_URL = 'http://your-jfrog-url'
        JFROG_CREDENTIALS_ID = 'your-jfrog-credentials-id'
        SONAR_URL = 'http://your-sonar-url'
        SONAR_TOKEN = 'your-sonar-token'
        AWS_EC2_INSTANCE = 'your-ec2-instance'
        AWS_EC2_CREDENTIALS_ID = 'your-ec2-credentials-id'
    }

    stages {
        stage('Code Checkout') {
            steps {
                git url: "${REPO_URL}", branch: "${BRANCH}"
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
                // Code quality analysis steps
                echo 'Code Analysis done'
            }
        }

        stage('Upload Artifacts') {
            steps {
                // Upload artifacts steps
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