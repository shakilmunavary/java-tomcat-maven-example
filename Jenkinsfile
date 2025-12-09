pipeline {
    agent any
    options {
        disableConcurrentBuilds()
        timestamps()
    }
    triggers {
        pollSCM('H/5 * * * *') // or configure Git webhook trigger
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
                        error('CODE_REPO_URL is required for the pipeline')
                    }
                    if (!env.DEFAULT_BRANCH?.trim()) {
                        error('DEFAULT_BRANCH is required for the pipeline')
                    }
                    if (!env.CHECKOUT_CRED_ID?.trim()) {
                        error('CHECKOUT_CRED_ID is required for checkout')
                    }
                }
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: "*/${env.DEFAULT_BRANCH}"]],
                    doGenerateSubmoduleConfigurations: false,
                    submoduleCfg: [],
                    extensions: [
                        [$class: 'CleanBeforeCheckout']
                    ],
                    userRemoteConfigs: [[
                        url: env.CODE_REPO_URL,
                        credentialsId: env.CHECKOUT_CRED_ID
                    ]]
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
                junit '**/target/surefire-reports/*.xml'
            }
        }
        stage('static-scan') {
            steps {
                script {
                    if (!env.SONAR_TOKEN?.trim()) {
                        error('SONAR_TOKEN is required to run SonarQube analysis')
                    }
                    def qualityGateWait = env.SKIP_QUALITY_GATE == 'true' ? 'false' : 'true'
                    withSonarQubeEnv('Mysonar') {
                        ansiColor('xterm') {
                            sh """
                                mvn -B sonar:sonar \
                                  -Dsonar.host.url=$SONAR_HOST_URL \
                                  -Dsonar.login=$SONAR_TOKEN \
                                  -Dsonar.qualitygate.wait=${qualityGateWait}
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
// [CICD_CODE_GENERATION_COMPLETE]