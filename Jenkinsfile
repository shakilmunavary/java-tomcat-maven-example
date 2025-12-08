pipeline {
    agent any
    options {
        timestamps()
    }
    triggers {
        // Uncomment the line below to enable SCM polling if webhooks are unavailable.
        // pollSCM('H/5 * * * *')
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
                        error('CODE_REPO_URL is required for the pipeline to proceed.')
                    }
                    if (!env.DEFAULT_BRANCH?.trim()) {
                        error('DEFAULT_BRANCH must be defined for the checkout stage.')
                    }
                }
                ansiColor('xterm') {
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: "*/${env.DEFAULT_BRANCH}"]],
                        doGenerateSubmoduleConfigurations: false,
                        extensions: [],
                        userRemoteConfigs: [[url: env.CODE_REPO_URL, credentialsId: env.CHECKOUT_CRED_ID]]
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
                    junit 'target/surefire-reports/*.xml'
                }
            }
        }
        stage('static-scan') {
            environment {
                SKIP_QUALITY_GATE = 'true'
            }
            steps {
                withSonarQubeEnv('Mysonar') {
                    ansiColor('xterm') {
                        sh 'mvn -B sonar:sonar -Dsonar.projectKey=appName -Dsonar.host.url=${env.SONAR_HOST_URL}'
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
// **[CICD_CODE_GENERATION_COMPLETE]**