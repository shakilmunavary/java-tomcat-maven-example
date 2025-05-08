pipeline {
    agent any
    stages {
        stage('Code Checkout') {
            steps {
                git url: 'https://github.com/shakilmunavary/java-tomcat-maven-example.git', branch: 'master'
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
                // Code quality analysis steps go here
                echo 'Code Analysis done'
            }
        }
        stage('Upload Artifacts') {
            steps {
                // Upload artifacts steps go here
                echo 'Upload Artifacts done'
            }
        }
        stage('Deployment') {
            steps {
                // Deploy to AWS EC2
                sh 'sudo cp target/java-tomcat-maven-example.war /opt/tomcat/webapps/'
            }
        }
    }
}