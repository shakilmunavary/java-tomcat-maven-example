pipeline {
    agent any
    environment {
        APP_NAME = 'app'
        ENV = 'Dev'
        CI_CD_TOOL = 'Jenkins'
        VCS = 'Github'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        FILE_REPO = 'Jfrog'
        TECH_STACK = 'Java'
        CODE_ANALYSIS_TOOL = 'Sonar'
        TARGET_ENV = 'AWS EC2'
        MAVEN_HOME = '/opt/maven'
        TOMCAT_HOME = '/opt/tomcat'
    }
    stages {
        stage('Code Checkout') {
            steps {
                git branch: 'master', url: "${REPO_URL}"
            }
        }
        stage('Build') {
            steps {
                sh '${MAVEN_HOME}/bin/mvn clean install'
            }
        }
        stage('Unit Testing') {
            steps {
                sh '${MAVEN_HOME}/bin/mvn test'
            }
        }
        stage('Code Quality Analysis') {
            steps {
                // Add your code quality analysis command here
                echo 'Code Analysis done'
            }
        }
        stage('Upload Artifacts') {
            steps {
                // Add your artifact upload command here
                echo 'Upload Artifacts done'
            }
        }
        stage('Deployment') {
            steps {
                sh 'sudo cp target/java-tomcat-maven-example.war ${TOMCAT_HOME}/webapps'
            }
        }
    }
}