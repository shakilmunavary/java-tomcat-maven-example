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
                echo 'Code Analysis done'
                // sh 'sonar-scanner'
            }
        }
        stage('Upload Artifacts') {
            steps {
                echo 'Upload Artifacts done'
                // sh 'jfrog rt u "target/*.war"'
            }
        }
        stage('Deployment') {
            steps {
                sh 'sudo cp target/java-tomcat-maven-example.war /opt/tomcat/webapps'
            }
        }
    }
    post {
        always {
            junit 'target/surefire-reports/TEST-*.xml'
        }
    }
}