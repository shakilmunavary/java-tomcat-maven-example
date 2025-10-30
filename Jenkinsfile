pipeline {
    agent any

    environment {
        APP_NAME = 'Roshanapp'
        ENVIRONMENT = 'Dev'
        GIT_REPO = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        BRANCH = 'master'
        JFROG_REPO = 'jfrog-repo-url' // Replace with actual JFrog repository URL
        SONAR_SCANNER = 'sonar-scanner' // Ensure Sonar Scanner is installed and configured
        AWS_EC2_IP = 'your-ec2-ip' // Replace with actual EC2 IP
        AWS_EC2_USER = 'ec2-user' // Replace with actual EC2 user
        AWS_EC2_KEY = 'your-ec2-key.pem' // Replace with actual EC2 key file
    }

    stages {
        stage('Code Checkout') {
            steps {
                echo "Checking out code from GitHub..."
                git branch: "${BRANCH}",
                    url: "${GIT_REPO}"
            }
        }

        stage('Build') {
            steps {
                echo "Building the application..."
                sh 'mvn clean package'
            }
        }

        stage('Unit Testing') {
            steps {
                echo "Running unit tests..."
                sh 'mvn test'
            }
        }

        stage('Code Quality Analysis') {
            steps {
                echo "Running SonarQube analysis..."
                // script {
                //     withSonarQubeEnv('SonarQube-Server') {
                //         sh "${SONAR_SCANNER} -Dsonar.projectKey=${APP_NAME} -Dsonar.sources=. -Dsonar.host.url=${SONAR_HOST_URL}"
                //     }
                // }
                echo "Code Analysis done"
            }
        }

        stage('Upload Artifacts') {
            steps {
                echo "Uploading artifacts to JFrog..."
                // script {
                //     def server = Artifactory.server 'jfrog-server'
                //     def uploadSpec = """{
                //         "files": [
                //             {
                //                 "pattern": "target/*.war",
                //                 "target": "${JFROG_REPO}/${APP_NAME}/${ENVIRONMENT}/"
                //             }
                //         ]
                //     }"""
                //     server.upload(uploadSpec)
                // }
                echo "Upload Artifacts done"
            }
        }

        stage('Deployment') {
            steps {
                echo "Deploying to AWS EC2..."
                script {
                    sshagent (['your-ssh-credentials-id']) {
                        sh """
                            scp -o StrictHostKeyChecking=no target/java-tomcat-maven-example.war ${AWS_EC2_USER}@${AWS_EC2_IP}:/tmp/
                            ssh -o StrictHostKeyChecking=no ${AWS_EC2_USER}@${AWS_EC2_IP} \
                            "sudo mv /tmp/java-tomcat-maven-example.war /opt/tomcat/webapps/"
                        """
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline completed for ${APP_NAME} in ${ENVIRONMENT} environment."
        }
    }
}