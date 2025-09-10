pipeline {
    agent any

    environment {
        APP_NAME = 'myapp1'
        ENVIRONMENT = 'Dev'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        BRANCH = 'master'
        TARGET_ENV = 'AWS EC2'
        EMAIL_RECIPIENT = 'roshan@admin.com'
    }

    stages {
        stage('Code Checkout') {
            steps {
                echo "Checking out code from ${REPO_URL}, branch: ${BRANCH}"
                git branch: "${BRANCH}", url: "${REPO_URL}"
            }
        }

        stage('Build') {
            steps {
                echo "Building the application"
                sh 'mvn clean package'
            }
        }

        stage('Unit Testing') {
            steps {
                echo "Running unit tests"
                sh 'mvn test'
            }
        }

        stage('Code Quality Analysis') {
            steps {
                echo "Running SonarQube analysis"
                // withSonarQubeEnv('SonarQube') {
                //     sh 'mvn sonar:sonar'
                // }
                echo "Code Analysis done"
            }
        }

        stage('Upload Artifacts') {
            steps {
                echo "Uploading artifacts to JFrog"
                // rtUpload(
                //     serverId: 'JFrog-Platform',
                //     spec: """{
                //         "files": [
                //             {
                //                 "target": "myapp1-dev-local/",
                //                 "includePattern": "target/*.war",
                //                 "recursive": "false",
                //                 "flat": "true"
                //             }
                //         ]
                //     }"""
                // )
                echo "Upload Artifacts done"
            }
        }

        stage('Deployment') {
            steps {
                echo "Deploying to ${TARGET_ENV}"
                if ("${TARGET_ENV}" == 'AWS EC2') {
                    echo "Copying java-tomcat-maven-example.war to Tomcat webapps"
                    sh 'sudo cp target/java-tomcat-maven-example.war /opt/tomcat/webapps/'
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline succeeded. Sending success email to ${EMAIL_RECIPIENT}"
            emailext (
                subject: "Pipeline Success: ${APP_NAME} in ${ENVIRONMENT}",
                body: "The pipeline for ${APP_NAME} in the ${ENVIRONMENT} environment has succeeded. Check the console output at ${BUILD_URL}",
                to: "${EMAIL_RECIPIENT}"
            )
        }
        failure {
            echo "Pipeline failed. Sending failure email to ${EMAIL_RECIPIENT}"
            emailext (
                subject: "Pipeline Failed: ${APP_NAME} in ${ENVIRONMENT}",
                body: "The pipeline for ${APP_NAME} in the ${ENVIRONMENT} environment has failed. Check the console output at ${BUILD_URL}",
                to: "${EMAIL_RECIPIENT}"
            )
        }
    }
}