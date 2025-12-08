pipeline {
    agent any
    options {
        timestamps()
        disableConcurrentBuilds()
    }
    triggers {
        // Configure a Git webhook or adjust polling as required.
        pollSCM('H/5 * * * *')
    }
    environment {
        CODE_REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        DEFAULT_BRANCH = 'master'
        CHECKOUT_CRED_ID = 'Roshan-Github'
        SONAR_HOST_URL = 'http://10.0.3.123:9000/sonar/'
        SKIP_QUALITY_GATE = 'true'
    }
    stages {
        stage('checkout') {
            steps {
                script {
                    if (!env.CODE_REPO_URL) {
                        error 'CODE_REPO_URL is required but not provided.'
                    }
                }
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: "*/${env.DEFAULT_BRANCH}"]],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [],
                    userRemoteConfigs: [[url: env.CODE_REPO_URL, credentialsId: env.CHECKOUT_CRED_ID]]
                ])
            }
        }
        stage('build') {
            steps {
                ansiColor('xterm') {
                    sh 'mvn -B -U clean package -DskipTests=false'
                }
            }
        }
        stage('unit-tests') {
            steps {
                ansiColor('xterm') {
                    sh 'mvn -B test'
                }
                junit 'target/surefire-reports/*.xml'
            }
        }
        stage('static-scan') {
            steps {
                ansiColor('xterm') {
                    withEnv(["SKIP_QUALITY_GATE=${env.SKIP_QUALITY_GATE}"]) {
                        withSonarQubeEnv('Mysonar') {
                            sh """
                                mvn -B sonar:sonar \
                                    -Dsonar.host.url=${env.SONAR_HOST_URL} \
                                    -Dsonar.projectKey=sonarProjectKey \
                                    -DskipTests=true
                            """
                        }
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