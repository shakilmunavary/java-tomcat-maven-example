pipeline {
    agent any
    environment {
        APPLICATION = "Application"
        ENVIRONMENT = "Dev"
        CI_CD_TOOL = "Jenkins"
        VCS = "Github"
        REPOSITORY_URL = "https://github.com/shakilmunavary/java-tomcat-maven-example.git"
        FILE_REPOSITORY_SYSTEM = "Jfrog"
        TECH_STACK = "Java"
        CODE_ANALYSIS_TOOL = "Sonar"
        TARGET_ENVIRONMENT = "AWS EC2"
        EXTRA_INPUT = "sh 'echo Job completed successfully; echo Sending email to roshan@example.com;'"
    }
    stages {
        stage('Code Checkout') {
            steps {
                git branch: 'master', url: "${REPOSITORY_URL}"
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
                // Code analysis steps go here
                // As per your request, I'm adding an echo command instead
                sh 'echo Code Analysis done'
            }
        }
        stage('Upload Artifacts') {
            steps {
                // Artifact upload steps go here
                // As per your request, I'm adding an echo command instead
                sh 'echo Upload Artifacts done'
            }
        }
        stage('Deployment') {
            steps {
                script {
                    if ("${TARGET_ENVIRONMENT}" == "AWS EC2") {
                        sh 'sudo cp target/java-tomcat-maven-example.war /opt/tomcat/webapp/'
                    }
                    // Add deployment steps here based on the target environment
                }
            }
        }
    }
    post {
        success {
            script {
                if ("${EXTRA_INPUT}" == "send email to roshan@example.com") {
                    sh 'echo Sending email to roshan@example.com'
                    // Add email sending code here
                }
            }
        }
    }
}