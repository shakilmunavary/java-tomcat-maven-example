pipeline {
    agent any

    environment {
        APP_NAME = 'ApplicationJava'
        ENVIRONMENT = 'Dev'
        REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        BRANCH = 'master'
        JFROG_REPO = 'your_jfrog_repo_url'
        SONAR_PROJECT_KEY = 'your_sonar_project_key'
        SONAR_ORGANIZATION = 'your_sonar_organization'
        SONAR_TOKEN = credentials('sonar_token')
        AWS_EC2_INSTANCE = 'your_aws_ec2_instance'
        AWS_EC2_USER = 'your_aws_ec2_user'
        AWS_EC2_KEY = credentials('aws_ec2_key')
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
                // Code Quality Analysis
                sh 'mvn sonar:sonar -Dsonar.projectKey=${SONAR_PROJECT_KEY} -Dsonar.organization=${SONAR_ORGANIZATION} -Dsonar.login=${SONAR_TOKEN}'
                echo 'Code Analysis done'
            }
        }

        stage('Upload Artifacts') {
            steps {
                // Upload Artifacts
                sh 'curl -u ${JFROG_USER}:${JFROG_PASSWORD} -T target/java-tomcat-maven-example.war ${JFROG_REPO}'
                echo 'Upload Artifacts done'
            }
        }

        stage('Deployment') {
            steps {
                script {
                    if (env.ENVIRONMENT == 'Dev') {
                        sh '''
                            ssh -i ${AWS_EC2_KEY} ${AWS_EC2_USER}@${AWS_EC2_INSTANCE} "sudo cp /path/to/target/java-tomcat-maven-example.war /opt/tomcat/webapps/"
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            mail to: "${EMAIL_RECIPIENT}",
                 subject: "Pipeline Status for ${APP_NAME}",
                 body: "The pipeline for ${APP_NAME} has completed. Check the console output for details."
        }
    }
}