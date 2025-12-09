pipeline {
    agent any

    environment {
        CODE_REPO_URL   = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        DEFAULT_BRANCH  = 'master'
        CHECKOUT_CRED_ID = 'Roshan-Github'
        SONAR_HOST_URL  = 'http://10.0.3.123:9000/sonar/'
        SKIP_QUALITY_GATE = 'true'
    }

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    triggers {
        // Uncomment one of the following as needed:
        // pollSCM('H/5 * * * *')
        // Generic webhook trigger can be configured in Jenkins job UI
    }

    stages {
        stage('Validate Configuration') {
            steps {
                script {
                    if (!env.CODE_REPO_URL?.trim()) {
                        error "CODE_REPO_URL is not defined. Failing early."
                    }
                    if (!env.DEFAULT_BRANCH?.trim()) {
                        error "DEFAULT_BRANCH is not defined. Failing early."
                    }
                }
            }
        }

        stage('checkout') {
            steps {
                script {
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: "*/${env.DEFAULT_BRANCH}"]],
                        userRemoteConfigs: [[
                            url: env.CODE_REPO_URL,
                            credentialsId: env.CHECKOUT_CRED_ID
                        ]]
                    ])
                }
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
                junit allowEmptyResults: true, testResults: 'target/surefire-reports/*.xml'
            }
        }

        stage('static-scan') {
            environment {
                // SonarQube environment name configured in Jenkins global config
                SONARQUBE_ENV = 'Mysonar'
            }
            steps {
                withSonarQubeEnv("${SONARQUBE_ENV}") {
                    sh """
                        mvn -B sonar:sonar \
                          -Dsonar.host.url=${SONAR_HOST_URL}
                    """
                }
            }
        }

        stage('SonarQube Quality Gate') {
            when {
                expression { return env.SKIP_QUALITY_GATE?.toBoolean() == false }
            }
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    script {
                        def qg = waitForQualityGate()
                        if (qg.status != 'OK') {
                            error "Pipeline aborted due to SonarQube quality gate failure: ${qg.status}"
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Build finished with status: ${currentBuild.currentResult}"
        }
        failure {
            echo 'Build failed.'
        }
        success {
            echo 'Build succeeded.'
        }
        cleanup {
            echo 'Cleaning workspace...'
            cleanWs()
        }
    }
}
**[CICD_CODE_GENERATION_COMPLETE]**