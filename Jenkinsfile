pipeline {
    agent any
    options {
        skipDefaultCheckout()
        timestamps()
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
                    if (!env.CODE_REPO_URL?.trim()) {
                        error('CODE_REPO_URL is not set. Aborting pipeline.')
                    }
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
        stage('build') {
            steps {
                sh 'mvn -B -U clean package -DskipTests=false'
            }
        }
        stage('unit-tests') {
            steps {
                sh 'mvn -B test'
                junit '**/target/surefire-reports/*.xml'
            }
        }
        stage('static-scan') {
            steps {
                withSonarQubeEnv('Mysonar') {
                    sh '''
                        mvn -B sonar:sonar \
                            -Dsonar.projectKey=appName \
                            -Dsonar.host.url=${SONAR_HOST_URL} \
                            -Dsonar.qualitygate.wait=true
                    '''.stripIndent().trim()
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