pipeline {
    agent any

    environment {
        APP_NAME = "add"
        ENV = "Dev"
        CI_CD_TOOL = "Jenkins"
        VCS_TOOL = "Github"
        REPO_URL = "https://github.com/shakilmunavary/java-tomcat-maven-example.git"
        FILE_REPO = "Jfrog"
        TECH_STACK = "Java"
        CODE_ANALYSIS_TOOL = "Sonar"
        TARGET_ENV = "AWS EC2"
    }

    stages {
        stage('Code Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: "${REPO_URL}"]]])
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
                // Code quality analysis steps here
                // sh 'sonar-scanner ...'
            }
        }

        stage('Upload Artifacts') {
            steps {
                // Upload artifacts steps here
                // sh 'jfrog upload ...'
            }
        }

        stage('Deployment') {
            when {
                environment name: 'TARGET_ENV', value: 'AWS EC2'
            }
            steps {
                sh 'sudo systemctl stop tomcat'
                sh 'sudo cp target/${APP_NAME}.jar /opt/tomcat/webapps/'
                sh 'sudo systemctl start tomcat'
            }
        }
    }
}