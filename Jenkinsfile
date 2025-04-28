Groovy
pipeline {
    agent any
    environment {
        APP_NAME = 'ABC'
        ENV = 'Dev'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example'
        FILE_REPO = 'Jfrog'
        TECH_STACK = 'Java'
        QUALITY_TOOLS = 'Sonar'
        TARGET_ENV = 'VM'
    }
    stages {
        stage('Checkout') {
            steps {
                git url: "$REPO_URL"
            }
        }
        stage('Build') {
            steps {
                sh 'mvn clean install'
            }
        }
        stage('Code Quality') {
            steps {
                script {
                    def scannerHome = tool 'sonar'
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
            post {
                always {
                    junit '**/target/surefire-reports/TEST-*.xml'
                }
            }
        }
        stage('Deploy to Jfrog') {
            steps {
                script {
                    jfrogPublishBuildInfo()
                }
            }
        }
        stage('Deploy to VM') {
            steps {
                sh 'ansible-playbook -i inventory.ini deploy.yml'
            }
        }
    }
}