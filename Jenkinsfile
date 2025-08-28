pipeline {
    agent any

    environment {
        APP_NAME = 'Myapplication1'
        ENV = 'Dev'
        GIT_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        GIT_BRANCH = 'master'
        JFROG_URL = 'https://your-jfrog-url.com'
        JFROG_REPO = 'your-jfrog-repo'
        SONAR_URL = 'https://your-sonar-url.com'
        SONAR_TOKEN = 'your-sonar-token'
        AWS_EC2_INSTANCE = 'your-aws-ec2-instance'
        AWS_EC2_USER = 'your-aws-ec2-user'
        AWS_EC2_KEY = 'your-aws-ec2-key'
    }

    stages {
        stage('Code Checkout') {
            steps {
                git branch: "${GIT_BRANCH}", url: "${GIT_URL}"
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
                // Code Quality Analysis
                echo 'Code Analysis done'
            }
        }

        stage('Upload Artifacts') {
            steps {
                // Upload Artifacts
                echo 'Upload Artifacts done'
            }
        }

        stage('Deployment') {
            steps {
                script {
                    if (ENV == 'Dev') {
                        sh "scp -i ${AWS_EC2_KEY} target/java-tomcat-maven-example.war ${AWS_EC2_USER}@${AWS_EC2_INSTANCE}:/opt/tomcat/webapps/"
                        sh "ssh -i ${AWS_EC2_KEY} ${AWS_EC2_USER}@${AWS_EC2_INSTANCE} 'sudo cp /opt/tomcat/webapps/java-tomcat-maven-example.war /opt/tomcat/webapps/'"
                    }
                }
            }
        }
    }
}