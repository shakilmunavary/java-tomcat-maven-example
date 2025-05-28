pipeline {
    agent any

    environment {
        APP_NAME = "Myapplication"
        ENVIRONMENT = "Dev"
        CI_CD_TOOL = "Jenkins"
        VERSION_CONTROL = "Github"
        REPO_URL = "https://github.com/shakilmunavary/java-tomcat-maven-example.git"
        FILE_REPO = "Jfrog"
        TECH_STACK = "Java"
        CODE_ANALYSIS_TOOL = "Sonar"
        TARGET_ENV = "AWS EC2"
        ADDITIONAL_INPUTS = "roshan@example.com"
    }

    stages {
        stage('Code Checkout') {
            steps {
                git branch: 'master', url: "${REPO_URL}"
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
                // Add code analysis tool steps here
            }
        }

        stage('Upload Artifacts') {
            steps {
                echo 'Upload Artifacts done'
                // Add artifact upload steps here
            }
        }

        stage('Deployment') {
            steps {
                sh 'sudo cp target/java-tomcat-maven-example.war /opt/tomcat/webapps/'
            }
        }
    }

    post {
        success {
            mail to: "${ADDITIONAL_INPUTS}", subject: "${APP_NAME} build successful", body: "The build was successful."
        }
    }
}