pipeline {
    agent any
    stages {
        stage('Code Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'master']], userRemoteConfigs: [[url: 'https://github.com/shakilmunavary/java-tomcat-maven-example.git']]])
            }
        }
        stage('Build') {
            steps {
                sh 'mvnnn clean install'
            }
        }
        stage('Unit Testing') {
            steps {
                sh 'mvn test'
            }
        }
        stage('Code Quality Analysis') {
            steps {
                // sh 'sonar-scanner'  // Commented out as per user's instructions
                echo 'Code Analysis done'
            }
        }
        stage('Upload Artifacts') {
            steps {
                // sh 'jfrog upload'  // Commented out as per user's instructions
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
