pipeline {
  agent any

  // Triggers: uncomment/change as appropriate
  // For Git webhooks, configure the webhook in your Git hosting provider and comment out pollSCM below.
  // triggers { GenericTrigger(...) } // example for GitHub webhooks via plugin
  triggers { pollSCM('H/5 * * * *') } // polling every 5 minutes as a sensible default

  environment {
    // Required exposures
    CODE_REPO_URL   = "https://github.com/shakilmunavary/java-tomcat-maven-example.git"
    DEFAULT_BRANCH  = "main"
    // If you provide CHECKOUT_CRED_ID in Jenkins job/env, it will be used for checkout.
    // Leave empty if not using credentials for checkout.
    CHECKOUT_CRED_ID = "${env.CHECKOUT_CRED_ID ?: ''}"

    // External integrations (expected to be provided via Jenkins global/env or credentials)
    // SONAR_HOST_URL must be set in the Jenkins environment (no credentials are hardcoded here)
    SONAR_HOST_URL = "${env.SONAR_HOST_URL ?: ''}"

    // Nexus settings (provide NEXUS_URL and NEXUS_REPO via environment)
    NEXUS_URL = "${env.NEXUS_URL ?: ''}"
    NEXUS_REPO = "${env.NEXUS_REPO ?: 'releases'}"

    // Placeholders
    APP_NAME = "appName"
    SONAR_PROJECT_KEY = "sonarProjectKey"
  }

  options {
    timeout(time: 60, unit: 'MINUTES')
    timestamps()
    // Keep build logs trimmed
    ansiColor('xterm')
  }

  stages {
    stage('checkout') {
      steps {
        script {
          if (!env.CODE_REPO_URL?.trim()) {
            error "CODE_REPO_URL is not set. Aborting pipeline."
          }

          // Build Git SCM config; use credentials if CHECKOUT_CRED_ID provided
          def userRemote = [url: "${env.CODE_REPO_URL}"]
          if (env.CHECKOUT_CRED_ID?.trim()) {
            userRemote.credentialsId = env.CHECKOUT_CRED_ID
          }

          checkout([
            $class: 'GitSCM',
            branches: [[name: "*/${env.DEFAULT_BRANCH}"]],
            userRemoteConfigs: [ userRemote ]
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
      }
      post {
        always {
          // Publish JUnit reports; include typical Maven surefire/failsafe paths
          junit allowEmptyResults: true, testResults: 'target/surefire-reports/*.xml, target/failsafe-reports/*.xml'
        }
      }
    }

    stage('static-scan') {
      steps {
        // SONAR_TOKEN must be stored as a Jenkins credential (string) with id 'SONAR_TOKEN'
        withCredentials([string(credentialsId: 'SONAR_TOKEN', variable: 'SONAR_TOKEN')]) {
          script {
            if (!env.SONAR_HOST_URL?.trim()) {
              error "SONAR_HOST_URL is not set in environment. Please configure SonarQube host URL."
            }

            // Run Sonar analysis via Maven
            sh """
              mvn -B org.sonarsource.scanner.maven:sonar-maven-plugin:sonar \
                -Dsonar.host.url=${env.SONAR_HOST_URL} \
                -Dsonar.login=${SONAR_TOKEN} \
                -Dsonar.projectKey=${SONAR_PROJECT_KEY}
            """
          }
        }

        // Wait for the SonarQube quality gate result and fail the pipeline if it is not OK
        // Requires SonarQube Jenkins plugin (Wait for Quality Gate) to be configured
        timeout(time: 5, unit: 'MINUTES') {
          script {
            def qg = waitForQualityGate()
            if (!qg) {
              error "No Quality Gate result received from SonarQube."
            }
            if (qg.status != 'OK') {
              error "SonarQube Quality Gate failed: ${qg.status}. Failing the pipeline."
            } else {
              echo "SonarQube Quality Gate passed: ${qg.status}"
            }
          }
        }
      }
    }

    stage('package-artifact') {
      steps {
        // NEXUS_CREDENTIALS should be a Jenkins usernamePassword credential containing NEXUS_USER / NEXUS_PASSWORD
        withCredentials([usernamePassword(credentialsId: 'NEXUS_CREDENTIALS', usernameVariable: 'NEXUS_USER', passwordVariable: 'NEXUS_PASSWORD')]) {
          script {
            if (!env.NEXUS_URL?.trim()) {
              error "NEXUS_URL is not set in environment. Please configure Nexus URL."
            }

            // Locate built artifact (first jar in target)
            def jarPath = sh(script: "ls target/*.jar 2>/dev/null | head -n 1 || true", returnStdout: true).trim()
            if (!jarPath) {
              error "No JAR artifact found in target/. Ensure the build produced an artifact."
            }

            // Upload artifact to Nexus release repository.
            // NOTE: Adjust upload path/coordinates to match your Nexus layout (groupId/artifactId/version).
            // Here we upload with a timestamped name to avoid overwriting; modify as required.
            def targetName = "${APP_NAME}-${env.BUILD_NUMBER}.jar"
            sh """
              curl -u ${NEXUS_USER}:${NEXUS_PASSWORD} --fail --show-error --silent \
                --upload-file ${jarPath} \
                ${NEXUS_URL}/repository/${NEXUS_REPO}/${targetName}
            """
            echo "Uploaded ${jarPath} to ${NEXUS_URL}/repository/${NEXUS_REPO}/${targetName}"
          }
        }
      }
    }
  }

  post {
    success {
      echo "Pipeline completed successfully."
    }
    failure {
      echo "Pipeline failed. Check logs for details."
    }
    cleanup {
      // optional cleanup actions
    }
  }
}
