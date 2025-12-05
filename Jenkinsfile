```groovy
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
        SONAR_ENVIRONMENT = 'Mysonar'
        SKIP_QUALITY_GATE = 'true'
    }
    triggers {
        // Use webhook or polling as needed
        pollSCM('H/5 * * * *')
    }
    stages {
        stage('checkout') {
            steps {
                script {
                    if (!env.CODE_REPO_URL?.trim()) {
                        error 'CODE_REPO_URL is required'
                    }
                }
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: "*/${env.DEFAULT_BRANCH}"]],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [],
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
                junit allowEmptyResults: true, testResults: 'target/surefire-reports/*.xml'
            }
        }
        stage('static-scan') {
            environment {
                SONAR_ENV = "${env.SONAR_ENVIRONMENT}"
                SKIP_QG = "${env.SKIP_QUALITY_GATE}"
            }
            steps {
                withSonarQubeEnv(env.SONAR_ENVIRONMENT) {
                    ansiColor('xterm') {
                        sh '''
                            mvn -B sonar:sonar \
                                -Dsonar.host.url=${SONAR_HOST_URL} \
                                -Dsonar.projectKey=sonarProjectKey \
                                -Dsonar.qualitygate.wait=false
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
[CICD_CODE_GENERATION_COMPLETE]