pipeline {
    agent any
    tools {
        maven 'Maven'
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
            }
        }
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarServer') {
                    sh 'mvn sonar:sonar'
                }
            }
        }
        stage('Deploy to VM') {
            steps {
                // Add your deployment steps here. This could be a script that copies the built artifact to the VM and starts it.
            }
        }
    }
}