
pipeline {
    agent any
    environment {
        APP_NAME = "ABCD"
        ENV = "Dev"
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
                git url: "${REPO_URL}", branch: "${ENV}"
            }
        }
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('Code Analysis') {
            steps {
                script {
                    sonarQubequalityGate: true,
                    sonarProperties: [
                        sonar.projectKey: "${APP_NAME}",
                        sonar.projectName: "${APP_NAME}",
                        sonar.projectVersion: "${ENV}",
                        sonar.sources: 'src/main/java',
                        sonar.sourceEncoding: 'UTF-8',
                        sonar.java.binaries: 'target/classes',
                        sonar.junit.reportsPath: 'target/surefire-reports',
                        sonar.junit.reportsPattern: 'TEST-*.xml'
                    ]
                }
            }
        }
        stage('Artifact Repository') {
            steps {
                script {
                    def server = Artifactory.server 'jfrogServer'
                    def uploadSpec = """{
                        "files": [
                            {
                                "pattern": "target/*.jar",
                                "target": "${FILE_REPO}/${APP_NAME}/${ENV}/"
                            }
                        ]
                    }"""
                    server.upload spec: uploadSpec
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    if ("${TARGET_ENV}" == "VM") {
                        sshagent(['sshKey']) {
                            sh 'scp target/*.jar user@vm:/path'
                            sh 'ssh user@vm "sudo systemctl restart ${APP_NAME}"'
                        }
                    }
                    // else add logic for deploying to other environments
                }
            }
        }
    }
}
