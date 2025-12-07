pipeline {
    agent any
    options {
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
        pollSCM('H/15 * * * *')
        // For GitHub/GitLab webhooks, configure the webhook in the repository settings.
    }
    stages {
        stage('checkout') {
            steps {
                script {
                    if (!env.CODE_REPO_URL?.trim()) {
                        error 'CODE_REPO_URL must be provided to proceed with checkout.'
                    }
                    if (!env.DEFAULT_BRANCH?.trim()) {
                        error 'DEFAULT_BRANCH must be defined for checkout.'
                    }
                }
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: "*/${env.DEFAULT_BRANCH}"]],
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
                junit testResults: '**/target/surefire-reports/*.xml', allowEmptyResults: false
            }
        }
        stage('static-scan') {
            environment {
                SKIP_QUALITY_GATE = 'true'
            }
            steps {
                script {
                    if (!env.SONAR_TOKEN?.trim()) {
                        error 'SONAR_TOKEN must be provided for the SonarQube scan.'
                    }
                }
                withSonarQubeEnv('Mysonar') {
                    ansiColor('xterm') {
                        sh """
                            mvn sonar:sonar \
                                -Dsonar.host.url=${SONAR_HOST_URL} \
                                -Dsonar.login=${SONAR_TOKEN} \
                                -Dsonar.qualitygate.skip=${SKIP_QUALITY_GATE}
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
// [CICD_CODE_GENERATION_COMPLETE]