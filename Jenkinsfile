pipeline {
    agent any

    environment {
        APPLICATION_NAME = 'XYZ'
        ENVIRONMENT = 'Dev'
        CI_CD_TOOL = 'Jenkins'
        VERSION_CONTROL = 'Github'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        FILE_REPO = 'Jfrog'
        TECH_STACK = 'Java'
        CODE_ANALYSIS_TOOL = 'Sonar'
        TARGET_ENV = 'AWS EC2'
        BRANCH = 'master'
    }

    stages {
        stage('Code Checkout') {
            steps {
                echo 'Checking out code from Github repository'
                git branch: "${BRANCH}", url: "${REPO_URL}"
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application using Maven'
                sh 'mvn clean install'
            }
        }

        stage('Unit Testing') {
            steps {
                echo 'Running Unit Tests'
                sh 'mvn test'
            }
        }

        stage('Code Quality Analysis') {
            steps {
                echo 'Analyzing code quality using SonarQube'
                // Add the actual Sonar analysis command below
                echo 'Code Analysis done'
            }
        }

        stage('Upload Artifacts') {
            steps {
                echo 'Uploading artifacts to Jfrog'
                // Add the actual Jfrog upload command below
                echo 'Upload Artifacts done'
            }
        }

        stage('Deployment') {
            when {
                expression { "${TARGET_ENV}" == "AWS EC2" }
            }
            steps {
                echo 'Deploying application to AWS EC2'
                sh 'sudo cp target/java-tomcat-maven-example.war /opt/tomcat/webapp/'
            }
        }
    }
}