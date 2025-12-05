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
    }
    stages {
        stage('checkout') {
            steps {
                script {
                    if (!env.CODE_REPO_URL?.trim()) {
                        error 'CODE_REPO_URL must be provided for the checkout stage.'
                    }
                }
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: "*/${env.DEFAULT_BRANCH}"]],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [],
                    userRemoteConfigs: [[
                        credentialsId: env.CHECKOUT_CRED_ID,
                        url: env.CODE_REPO_URL
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
                ansiColor('xterm') {
                    withSonarQubeEnv('Mysonar') {
                        sh """
                            mvn -B sonar:sonar \
                                -Dsonar.projectKey=java-tomcat-maven-example \
                                -Dsonar.host.url=${env.SONAR_HOST_URL}
                        """
                    }
                }
                script {
                    if (env.SKIP_QUALITY_GATE?.toBoolean()) {
                        echo 'SKIP_QUALITY_GATE=true, skipping waitForQualityGate step.'
                    } else {
                        timeout(time: 2, unit: 'MINUTES') {
                            waitForQualityGate abortPipeline: true
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