pipeline {
    agent any
    options {
        disableConcurrentBuilds()
        timestamps()
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
                        error "CODE_REPO_URL is required to proceed with the pipeline."
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
                script {
                    ansiColor('xterm') {
                        withSonarQubeEnv('Mysonar') {
                            sh '''
                                mvn -B -DskipTests=true sonar:sonar \
                                    -Dsonar.projectKey=appName \
                                    -Dsonar.host.url=${SONAR_HOST_URL}
                            '''.stripIndent()
                        }
                    }
                    if (env.SKIP_QUALITY_GATE?.toBoolean()) {
                        echo 'Skipping SonarQube quality gate evaluation (SKIP_QUALITY_GATE=true).'
                    } else {
                        waitForQualityGate abortPipeline: true
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
[CICD_CODE_GENERATION_COMPLETE]