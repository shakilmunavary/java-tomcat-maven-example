pipeline {
    agent any

    environment {
        APP_NAME = 'KLMPP'
        ENVIRONMENT = 'Dev'
        GIT_REPO = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        BRANCH = 'master'
        JFROG_REPO = 'jfrog-repo-url' // Replace with actual JFrog repository URL
        SONAR_SERVER = 'sonar-server-url' // Replace with actual SonarQube server URL
        AWS_EC2_IP = 'ec2-instance-ip' // Replace with actual AWS EC2 instance IP
        TOMCAT_WEBAPP_DIR = '/opt/tomcat/webapp'
    }

    stages {
        stage('Code Checkout') {
            steps {
                echo "Checking out code from GitHub repository..."
                git branch: "${BRANCH}", url: "${GIT_REPO}"
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
                // echo "Running SonarQube analysis..."
                // withSonarQubeEnv('SonarQube') {
                //     sh "mvn sonar:sonar \
                //         -Dsonar.projectKey=${APP_NAME} \
                //         -Dsonar.projectName=${APP_NAME} \
                //         -Dsonar.host.url=${SONAR_SERVER}"
                // }
                echo "Code Analysis done"
            }
        }

        stage('Upload Artifacts') {
            steps {
                // echo "Uploading artifacts to JFrog..."
                // rtUpload(
                //     serverId: 'JFrog',
                //     spec: """{
                //         "files": [
                //             {
                //                 "target": "${JFROG_REPO}/${APP_NAME}/${ENVIRONMENT}/",
                //                 "pattern": "target/*.war",
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
                echo "Deploying to AWS EC2..."
                script {
                    if ("${ENVIRONMENT}" == "Dev" && "${TOMCAT_WEBAPP_DIR}" != "") {
                        sh """
                            scp -o StrictHostKeyChecking=no target/java-tomcat-maven-example.war ec2-user@${AWS_EC2_IP}:/tmp/
                            ssh -o StrictHostKeyChecking=no ec2-user@${AWS_EC2_IP} \
                            "sudo mv /tmp/java-tomcat-maven-example.war ${TOMCAT_WEBAPP_DIR}/"
                        """
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline completed."
        }
    }
}