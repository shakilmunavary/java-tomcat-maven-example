groovy
pipeline {
    agent any

    environment {
        APP_NAME = "ABC"
        ENVIRONMENT = "Dev"
        CICD_TOOLS = "Jenkins"
        REPO_DETAILS = "Github"
        REPO_URL = "https://github.com/shakilmunavary/java-tomcat-maven-example"
        FILE_REPO = "Jfrog"
        TECH_STACK = "Java"
        QUALITY_TOOLS = "Sonar"
        TARGET_ENV = "VM"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: '$REPO_URL'
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
                    withSonarQubeEnv('SonarServer') {
                        sh 'mvn sonar:sonar'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'mvn -Dmaven.test.skip=true package'
                sh 'java -jar target/*.war'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed'
            emailext(
                subject: "Pipeline: ${currentBuild.currentResult}",
                body: "Pipeline completed. Check console output at: ${env.BUILD_URL}",
                to: 'you@example.com'
            )
        }
    }
}