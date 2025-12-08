pipeline {
    agent any
    options {
        skipDefaultCheckout()
        timestamps()
        disableConcurrentBuilds()
    }
    environment {
        CODE_REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        DEFAULT_BRANCH = 'master'
        CHECKOUT_CRED_ID = 'Roshan-Github'
        SONAR_HOST_URL = 'http://10.0.3.123:9000/sonar/'
        SKIP_QUALITY_GATE = 'true'
    }
    triggers {
        pollSCM('H/5 * * * *')
        // For GitHub webhooks prefer: triggers { ghprbTrigger(...) } or use Git hook on the repo
    }
    stages {
        stage('checkout') {
            steps {
                script {
                    if (!env.CODE_REPO_URL?.trim()) {
                        error 'CODE_REPO_URL is required but not provided.'
                    }
                    if (!env.DEFAULT_BRANCH?.trim()) {
                        error 'DEFAULT_BRANCH is required but not provided.'
                    }
                }
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: "*/${env.DEFAULT_BRANCH}"]],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [[$class: 'CleanBeforeCheckout']],
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
            environment {
                SKIP_QUALITY_GATE = 'true'
            }
            steps {
                withSonarQubeEnv('Mysonar') {
                    ansiColor('xterm') {
                        sh """
                            mvn sonar:sonar \
                                -Dsonar.host.url=${env.SONAR_HOST_URL} \
                                -Dsonar.login=${env.SONAR_TOKEN ?: ''} \
                                -DskipTests=true \
                                -Dsonar.qualitygate.wait=${env.SKIP_QUALITY_GATE == 'true' ? 'false' : 'true'}
                        """
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