```groovy
pipeline {
    agent any
    environment {
        CODE_REPO_URL      = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        DEFAULT_BRANCH     = 'master'
        CHECKOUT_CRED_ID   = 'Roshan-Github'
        SONAR_HOST_URL     = 'http://10.0.3.123:9000/sonar/'
        SKIP_QUALITY_GATE  = 'true'
    }
    options {
        timestamps()
        disableConcurrentBuilds()
    }
    triggers {
        pollSCM('H/15 * * * *')
        // Uncomment the following line to enable GitHub webhook triggering:
        // GenericTrigger(...)
    }
    stages {
        stage('checkout') {
            steps {
                script {
                    if (!env.CODE_REPO_URL?.trim()) {
                        error('CODE_REPO_URL is required to proceed.')
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
            environment {
                SONAR_PROJECT_KEY = 'java-tomcat-maven-example'
            }
            steps {
                withCredentials([string(credentialsId: 'Sonar-Token', variable: 'SONAR_TOKEN')]) {
                    withSonarQubeEnv('Mysonar') {
                        sh '''
                            mvn -B -U sonar:sonar \
                                -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                                -Dsonar.host.url=${SONAR_HOST_URL} \
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
[CICD_CODE_GENERATION_COMPLETE]