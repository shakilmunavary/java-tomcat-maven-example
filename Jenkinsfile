pipeline {
    agent any
    options {
        skipDefaultCheckout()
        timestamps()
        disableConcurrentBuilds()
    }
    triggers {
        pollSCM('H/15 * * * *') // replace with SCM webhook trigger if available
    }
    environment {
        CODE_REPO_URL       = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        DEFAULT_BRANCH      = 'master'
        CHECKOUT_CRED_ID    = 'Roshan-Github'
        SONAR_HOST_URL      = 'http://10.0.3.123:9000'
        NEXUS_URL           = 'https://nexus.example.com'
        NEXUS_RELEASE_REPO  = 'maven-snapshots'
    }
    stages {
        stage('checkout') {
            steps {
                script {
                    if (!env.CODE_REPO_URL?.trim()) {
                        error('CODE_REPO_URL is required to proceed with the pipeline')
                    }
                }
                deleteDir()
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: env.DEFAULT_BRANCH]],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [[$class: 'CloneOption', shallow: false, depth: 0, noTags: false]],
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
                junit allowEmptyResults: false, testResults: '**/target/surefire-reports/*.xml'
            }
        }
        stage('static-scan') {
            steps {
                ansiColor('xterm') {
                        withSonarQubeEnv('Mysonar') {
                            sh '''
                                mvn -B -U verify sonar:sonar \
                                    -Dsonar.host.url=$SONAR_HOST_URL \
                                    -Dsonar.login=squ_c420c1867277e49dcf26ddd3dff8f1267a7f61e4 \
                                    -Dsonar.projectKey=simple-java-maven-app
                            '''
                        }
                    }
                }
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        
        stage('package-artifact') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'nexus-credentials-id', usernameVariable: 'NEXUS_USER', passwordVariable: 'NEXUS_PASSWORD')]) {
                    script {
                        def jarFile = sh(script: "ls target/*.jar | head -n 1", returnStdout: true).trim()
                        if (!jarFile) {
                            error('No JAR artifact found in target directory to publish')
                        }
                        def jarName = jarFile.tokenize('/').last()
                        ansiColor('xterm') {
                            sh """
                                curl --fail -u $NEXUS_USER:$NEXUS_PASSWORD \
                                    -T ${jarFile} \
                                    ${NEXUS_URL}/repository/${NEXUS_RELEASE_REPO}/${env.BUILD_ID}/${jarName}
                            """
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
