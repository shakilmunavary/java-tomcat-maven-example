pipeline {
    agent any
    options {
        timestamps()
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }
    environment {
        CODE_REPO_URL     = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        DEFAULT_BRANCH    = 'master'
        CHECKOUT_CRED_ID  = 'Roshan-Github'
        SONAR_HOST_URL    = 'http://10.0.3.123:9000/sonar/'
        SKIP_QUALITY_GATE = 'true'
        SONAR_PROJECT_KEY = 'java-app-sonar'
    }
    stages {
        stage('checkout') {
            steps {
                script {
                    if (!env.CODE_REPO_URL?.trim()) {
                        error('CODE_REPO_URL is required but not provided.')
                    }
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: "*/${env.DEFAULT_BRANCH}"]],
                        doGenerateSubmoduleConfigurations: false,
                        extensions: [
                            [$class: 'CleanBeforeCheckout'],
                            [$class: 'WipeWorkspace']
                        ],
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
                junit '**/target/surefire-reports/*.xml'
            }
        }
        stage('static-scan') {
            environment {
                SONAR_ENV = 'Mysonar'
            }
            steps {
                withSonarQubeEnv('Mysonar') {
                    ansiColor('xterm') {
                        sh '''
                            mvn -B sonar:sonar \
                                -Dsonar.host.url=${SONAR_HOST_URL} \
                                -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                                -Dsonar.qualitygate.wait=true \
                                -Dsonar.login=${SONAR_TOKEN} \
                                -DskipTests=true
                        '''
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