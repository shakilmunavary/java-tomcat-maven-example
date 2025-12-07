pipeline {
    agent any
    environment {
        CODE_REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        DEFAULT_BRANCH = 'master'
        CHECKOUT_CRED_ID = 'Roshan-Github'
        SONAR_HOST_URL = 'http://10.0.3.123:9000/sonar/'
    }
    options {
        timestamps()
        disableConcurrentBuilds()
    }
    triggers {
        // Enable GitHub webhooks or uncomment the line below for SCM polling
        // pollSCM('H/5 * * * *')
    }
    stages {
        stage('checkout') {
            steps {
                script {
                    if (!env.CODE_REPO_URL?.trim()) {
                        error('CODE_REPO_URL is required but not provided')
                    }
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: env.DEFAULT_BRANCH]],
                        doGenerateSubmoduleConfigurations: false,
                        extensions: [],
                        userRemoteConfigs: [[
                            url: env.CODE_REPO_URL,
                            credentialsId: env.CHECKOUT_CRED_ID
                        ]]
                    ])
                }
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
            }
            post {
                always {
                    junit '**/target/surefire-reports/*.xml'
                }
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