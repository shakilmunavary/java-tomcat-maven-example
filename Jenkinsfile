pipeline {
    agent any

    environment {
        APP_NAME = 'Myapplication'
        ENV = 'Dev'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        BRANCH = 'master'
        JFROG_URL = 'http://your-jfrog-url'
        JFROG_REPO = 'your-jfrog-repo'
        SONAR_URL = 'http://your-sonar-url'
        SONAR_TOKEN = 'your-sonar-token'
        TARGET_ENV = 'AWS EC2'
        EMAIL_RECIPIENT = 'roshan@example.com'
    }

    stages {
        stage('Code Checkout') {
            steps {
                git branch: "${BRANCH}", url: "${REPO_URL}"
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
                // Code quality analysis
                echo 'Code Analysis done'
            }
        }

        stage('Upload Artifacts') {
            steps {
                // Upload artifacts
                echo 'Upload Artifacts done'
            }
        }

        stage('Deployment') {
            steps {
                script {
                    if (env.TARGET_ENV == 'AWS EC2') {
                        sh 'sudo cp target/java-tomcat-maven-example.war /opt/tomcat/webapps/'
                    }
                }
            }
        }
    }

    post {
        success {
            mail to: "${EMAIL_RECIPIENT}",
                 subject: "Build Success for ${APP_NAME}",
                 body: "The build for ${APP_NAME} in ${ENV} environment was successful."
        }
    }
}