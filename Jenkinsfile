pipeline {
  agent any
  environment {
    APP_NAME = 'app'
    ENV = 'Dev'
    CI_CD_TOOL = 'Jenkins'
    VCS = 'Github'
    REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
    FILE_REPO_SYSTEM = 'Jfrog'
    TECH_STACK = 'Java'
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
        // Code quality analysis steps would go here
      }
    }
    stage('Upload Artifacts') {
      steps {
        echo 'Upload Artifacts done'
        // Artifact upload steps would go here
      }
    }
    stage('Deployment') {
      steps {
        sh 'sudo cp java-tomcat-maven-example.war /opt/tomcat/webapp'
      }
    }
  }
}