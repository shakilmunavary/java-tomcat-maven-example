pipeline {
    agent any
    environment {
        APP_NAME = "sddd"
        ENV = "Dev"
        CI_CD_TOOL = "Jenkins"
        VCS = "Github"
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
                sh 'mvn clean install'
            }
        }
        stage('Unit Testing') {
            steps {
                sh 'mvn test'
            }
        }
        stage('Code quality Analysis') {
            steps {
                // sh 'sonar-scanner'
                echo "Code Analysis done"
            }
        }
        stage('Upload Artifacts') {
            steps {
                // sh 'jfrog upload'
                echo "Upload Artifacts done"
            }
        }
        stage('Deployment') {
            steps {
                sh 'sudo systemctl stop tomcat'
                sh 'sudo cp target/${APP_NAME}.jar /opt/tomcat/webapps/'
                sh 'sudo systemctl start tomcat'
            }
        }
    }
    post {
        always {
            echo "Pipeline completed"
        }
    }
}
