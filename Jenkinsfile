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
        SKIP_QUALITY_GATE = 'true'
    }
    triggers {
        // Prefer Git push PR webhooks; fallback to polling if not available.
        pollSCM('H/5 * * * *')
    }
    stages {
        stage('checkout') {
            steps {
                script {
                    if (!env.CODE_REPO_URL?.trim()) {
                        error('CODE_REPO_URL is required to continue.')
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
                ansiColor('xterm') {
                    withSonarQubeEnv('Mysonar') {
                        sh '''
                            mvn sonar:sonar \
                              -Dsonar.host.url=${SONAR_HOST_URL} \
                              -Dsonar.projectKey=java-tomcat-maven-example \
                              -Dsonar.login=${SONAR_TOKEN}
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