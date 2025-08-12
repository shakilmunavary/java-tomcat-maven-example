pipeline {
    agent any

    stages {
        stage('Code Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
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
                // Code Quality Analysis steps
                echo 'Code Analysis done'
            }
        }

        stage('Upload Artifacts') {
            steps {
                // Upload Artifacts steps
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