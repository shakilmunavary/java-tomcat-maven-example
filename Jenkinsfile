pipeline {
    agent any
    environment {
        APP_NAME = 'app1'
        ENVIRONMENT = 'Dev'
        CI_CD_TOOL = 'Jenkins'
        VCS = 'Github'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        FILE_REPO = 'Jfrog'
        CODE_STACK = 'Java'
        CODE_ANALYSIS_TOOL = 'Sonar'
        TARGET_ENV = 'AWS EC2'
    }
    stages {
        stage('Code Checkout') {
            steps {
                git branch: 'master', url: "${REPO_URL}"
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
                // Code analysis tool steps are commented out
                // sh 'sonar-scanner ...'
                echo 'Code Analysis done'
            }
        }
        stage('Upload Artifacts') {
            steps {
                // Artifact upload steps are commented out
                // sh 'jfrog cli ...'
                echo 'Upload Artifacts done'
            }
        }
        stage('Deployment') {
            steps {
                script {
                    if ("${TARGET_ENV}" == "AWS EC2") {
                        sh 'cp target/java-tomcat-maven-example.war /opt/tomcat/webapps/'
                    }
                }
            }
        }
    }
}