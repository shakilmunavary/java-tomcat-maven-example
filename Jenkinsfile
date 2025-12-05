pipeline {
    agent any
    options {
        timestamps()
        disableConcurrentBuilds()
    }
    triggers {
        pollSCM('H/5 * * * *')
    }
    environment {
        CODE_REPO_URL      = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        DEFAULT_BRANCH     = 'master'
        CHECKOUT_CRED_ID   = 'Roshan-Github'
        SONAR_HOST_URL     = 'http://10.0.3.123:9000/sonar/'
        SONAR_TOKEN        = credentials('sonar-token')
        SKIP_QUALITY_GATE  = 'true'
    }
    stages {
        stage('checkout') {
            steps {
                script {
                    if (!env.CODE_REPO_URL?.trim()) {
                        error 'CODE_REPO_URL is required to proceed with the pipeline.'
                    }
                }
                checkout([
                    $class           : 'GitSCM',
                    branches         : [[name: "*/${env.DEFAULT_BRANCH}"]],
                    doGenerateSubmoduleConfigurations: false,
                    extensions       : [
                        [$class: 'CleanCheckout'],
                        [$class: 'WipeWorkspace']
                    ],
                    userRemoteConfigs: [[
                        url          : "${env.CODE_REPO_URL}",
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
                junit 'target/surefire-reports/*.xml'
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
                            mvn -B sonar:sonar \
                              -Dsonar.host.url=${SONAR_HOST_URL} \
                              -Dsonar.projectKey=java-tomcat-maven-example \
                              -Dsonar.login=${SONAR_TOKEN} \
                              -Dsonar.qualitygate.wait=false
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