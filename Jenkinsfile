pipeline {
    agent any
    environment {
        APP_NAME = 'HelloWorldapp'
        ENV = 'Dev'
        CI_CD_TOOL = 'Jenkins'
        VCS = 'Github'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        FILE_REPO = 'Jfrog'
        TECH_STACK = 'Java'
        CODE_ANALYSIS_TOOL = 'Sonar'
        TARGET_ENV = 'AWS EC2'
        EMAIL = 'roshan@example.com'
    }
    stages {
        stage('Code Checkout') {
            steps {
                checkout scm: [$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: "${REPO_URL}"]]]
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
                // Code analysis tool steps goes here
                echo 'Code Analysis done'
            }
        }
        stage('Upload Artifacts') {
            steps {
                // File repository upload steps goes here
                echo 'Upload Artifacts done'
            }
        }
        stage('Deployment') {
            steps {
                sh 'sudo cp target/java-tomcat-maven-example.war /opt/tomcat/webapps/'
            }
        }
    }
    post {
        failure {
            mail to: "${EMAIL}", subject: "Build failed: ${APP_NAME} in ${ENV}", body: "The build of ${APP_NAME} in ${ENV} has failed. Please check the logs at ${BUILD_URL}"
        }
    }
}