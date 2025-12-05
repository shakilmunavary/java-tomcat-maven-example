pipeline {
    agent any
    options {
        skipDefaultCheckout(true)
        timestamps()
        disableConcurrentBuilds()
    }
    environment {
        CODE_REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        DEFAULT_BRANCH = 'master'
        CHECKOUT_CRED_ID = 'Roshan-Github'
        SONAR_HOST_URL = 'http://10.0.3.123:9000/sonar/'
    }
    triggers {
        pollSCM('H/5 * * * *')
        // For Git webhooks, configure in Jenkins job instead of here.
    }
    stages {
        stage('checkout') {
            steps {
                script {
                    if (!env.CODE_REPO_URL?.trim()) {
                        error('CODE_REPO_URL environment variable is required')
                    }
                }
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: "*/${env.DEFAULT_BRANCH}"]],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [
                        [$class: 'CleanBeforeCheckout']
                    ],
                    userRemoteConfigs: [
                        [
                            url: env.CODE_REPO_URL,
                            credentialsId: env.CHECKOUT_CRED_ID
                        ]
                    ]
                ])
            }
        }
        stage('build') {
            steps {
                sh 'mvn -B -U clean package -DskipTests=false'
            }
        }
        stage('unit-tests') {
            steps {
                sh 'mvn -B test'
                junit 'target/surefire-reports/*.xml'
            }
        }
        stage('static-scan') {
            environment {
                SKIP_QUALITY_GATE = 'true'
            }
            steps {
                withSonarQubeEnv('Mysonar') {
                    sh 'mvn -B sonar:sonar -Dsonar.host.url=${SONAR_HOST_URL}'
                }
                script {
                    def qg = waitForQualityGate()
                    if (qg.status != 'OK') {
                        error("SonarQube Quality Gate failed: ${qg.status}")
                    }
                }
            }
        }
    }
    post {
        cleanup {
            echo 'Cleaning workspace...'
            cleanWs()
        }
    }
}