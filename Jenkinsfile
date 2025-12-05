pipeline {
    agent any
    options {
        skipDefaultCheckout()
        timestamps()
    }
    environment {
        CODE_REPO_URL     = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        DEFAULT_BRANCH    = 'master'
        CHECKOUT_CRED_ID  = 'Roshan-Github'
        SONAR_HOST_URL    = 'http://10.0.3.123:9000/sonar/'
        SKIP_QUALITY_GATE = 'true'
    }
    triggers {
        pollSCM('H/15 * * * *')
    }
    stages {
        stage('checkout') {
            steps {
                script {
                    if (!env.CODE_REPO_URL?.trim()) {
                        error('CODE_REPO_URL must be supplied for the pipeline to proceed.')
                    }
                }
                git branch: "${env.DEFAULT_BRANCH}",
                    credentialsId: env.CHECKOUT_CRED_ID,
                    url: env.CODE_REPO_URL
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
                withSonarQubeEnv('Mysonar') {
                    ansiColor('xterm') {
                        sh """mvn -B sonar:sonar \
                            -Dsonar.projectKey=java-tomcat-maven-example \
                            -Dsonar.projectName=java-tomcat-maven-example \
                            -Dsonar.host.url=${env.SONAR_HOST_URL} \
                            -DskipTests=true \
                            -DskipQualityGate=${env.SKIP_QUALITY_GATE}
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