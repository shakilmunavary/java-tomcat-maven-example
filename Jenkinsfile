pipeline {
    agent any

    environment {
        // Always expose these
        CODE_REPO_URL = 'https://github.com/shakilmunavary/java-tomcat-maven-example.git'
        DEFAULT_BRANCH = 'main'
        // Replace with your Jenkins credentialsId for git checkout
        CHECKOUT_CRED_ID = 'Roshan-Github'

        // Placeholders for integration endpoints / repos (set in Jenkins global env or replace with proper values)
        SONAR_HOST_URL = 'http://10.0.3.123:9000'        // e.g. https://sonarqube.example.com
        NEXUS_URL      = ''        // e.g. https://nexus.example.com
        NEXUS_REPO     = 'nexus-release-repo' // repository name/path in Nexus where .jar should be uploaded

        // App placeholders
        APP_NAME       = 'SimpleApplication'
        SONAR_PROJECT_KEY = 'simple-java-maven-app'
    }

    options {
        timestamps()
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timeout(time: 60, unit: 'MINUTES')
    }

    // Recommended: trigger via Git webhook. Alternatively uncomment the pollSCM if needed:
    // triggers { pollSCM('H/5 * * * *') }

    stages {

        stage('validate') {
            steps {
                script {
                    if (!env.CODE_REPO_URL || env.CODE_REPO_URL.trim() == '') {
                        error("CODE_REPO_URL is not set. Failing pipeline.")
                    }
                    if (!env.DEFAULT_BRANCH || env.DEFAULT_BRANCH.trim() == '') {
                        error("DEFAULT_BRANCH is not set. Failing pipeline.")
                    }
                }
            }
        }

        stage('checkout') {
            steps {
                script {
                    // Dedicated checkout per requirement
                  checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'Roshan-Github', url: 'https://github.com/shakilmunavary/java-tomcat-maven-example.git']])
                    
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
                // Publish JUnit results
                junit allowEmptyResults: false, testResults: '**/target/surefire-reports/*.xml'
            }
        }

        stage('static-scan') {
            steps {
                // SonarQube token should be stored in Jenkins Credentials (string). Replace 'sonar-token-id' with your credentialsId.
            withSonarQubeEnv() {
                  sh "${mvn}/bin/mvn clean verify sonar:sonar -Dsonar.projectKey=simple-java-maven-app -Dsonar.projectName='simple-java-maven-app'"
            }

                // Wait for quality gate result and fail pipeline on non-OK
                script {
                    // waitForQualityGate requires SonarQube webhook configured to notify Jenkins.
                    timeout(time: 10, unit: 'MINUTES') {
                        def qg = waitForQualityGate()
                        if (qg == null) {
                            error "Quality gate check did not return a result. Ensure SonarQube webhook is configured."
                        } else if (qg.status != 'OK') {
                            error "Quality gate failed: ${qg.status} - ${qg}"
                        } else {
                            echo "Quality gate passed: ${qg.status}"
                        }
                    }
                }
            }
        }

        stage('package-artifact') {
            steps {
                // Upload artifact (.jar) to Nexus release repo
                // Use credentials stored in Jenkins (usernamePassword). Replace 'nexus-credentials-id' with your credentialsId.
                withCredentials([usernamePassword(credentialsId: 'nexus-credentials-id', usernameVariable: 'NEXUS_USER', passwordVariable: 'NEXUS_PASSWORD')]) {
                    
                        script {
                            // Find the jar (simple glob). Adjust if multiple jars are produced.
                            def jar = sh(script: "ls target/*.jar | head -n 1", returnStdout: true).trim()
                            if (!jar) {
                                error "No .jar found in target/. Build may have failed or packaging location is different."
                            }
                            echo "Uploading ${jar} to ${env.NEXUS_URL}/repository/${env.NEXUS_REPO}/"

                            // Use curl to upload. For Nexus3 raw or maven-hosted repo, the upload endpoint may differ.
                            // Adjust upload command as appropriate for your Nexus repository type.
                            sh """
                                curl -v --fail -u ${NEXUS_USER}:${NEXUS_PASSWORD} \
                                  --upload-file "${jar}" \
                                  "${env.NEXUS_URL}/repository/${env.NEXUS_REPO}/\$(basename ${jar})"
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
        failure {
            echo 'Build failed. See logs for details.'
        }
        success {
            echo "Pipeline completed successfully."
        }
    }
}
