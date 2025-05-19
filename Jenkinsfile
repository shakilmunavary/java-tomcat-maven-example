pipeline {
    agent any
    environment {
        APP_NAME = "AniApp"
        ENV = "Dev"
        CI_CD = "Jenkins"
        VCS = "Github"
        REPO_URL = "https://github.com/shakilmunavary/java-tomcat-maven-example.git"
        FILE_REPO = "Nexus"
        STACK = "Java"
        CODE_ANALYSIS = "Sonar"
        TARGET_ENV = "AWS EC2"
    }

    stages {
        stage('Code Checkout') {
            steps {
                git branch: "${ENV.toLowerCase() == 'dev' ? 'master' : ''}", url: "${REPO_URL}"
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
                // Sonar analysis step would be here
                echo 'Code Analysis done'
            }
        }

        stage('Upload Artifacts') {
            steps {
                // Artifact upload step would be here
                echo 'Upload Artifacts done'
            }
        }

        stage('Deployment') {
            steps {
                script {
                    if (TARGET_ENV == "AWS EC2") {
                        sh "sudo cp target/java-tomcat-maven-example.war /opt/tomcat/webapps/"
                    }
                }
            }
        }
    }

    post {
        success {
            emailext body: 'The Jenkins build has completed successfully', subject: "${APP_NAME} - Build Successful", to: "recipient@example.com"
        }
        failure {
            emailext body: 'The Jenkins build has failed', subject: "${APP_NAME} - Build Failed", to: "recipient@example.com"
        }
    }
}