python
import click

@click.command()
@click.option('--app-name', prompt='Enter the app name', help='The name of the application.')
@click.option('--environment', prompt='Enter the environment', help='The environment where the application will be deployed.')
@click.option('--cicd-tools', prompt='Enter the CICD tool', help='The CICD tool to be used.')
@click.option('--repo-details', prompt='Enter the repo details', help='The repository details.')
@click.option('--repo-url', prompt='Enter the repo URL', help='The repository URL.')
@click.option('--file-repo', prompt='Enter the file repository', help='The file repository.')
@click.option('--tech-stack', prompt='Enter the tech stack', help='The technology stack.')
@click.option('--quality-tools', prompt='Enter the code quality tool', help='The code quality tool.')
@click.option('--target-env', prompt='Enter the target environment', help='The target environment.')
@click.option('--additional-inputs', prompt='Enter additional inputs', help='Additional inputs for the pipeline.')
def generate_pipeline(app_name, environment, cicd_tools, repo_details, repo_url, file_repo, tech_stack, quality_tools, target_env, additional_inputs):
    pipeline_script = f"""
pipeline {{
    agent {{ any }}
    stages {{
        stage('Checkout') {{
            steps {{
                git url: '{repo_url}', branch: 'main'
            }}
        }}
        stage('Build') {{
            steps {{
                sh 'mvn clean package'
            }}
        }}
        stage('Quality Check') {{
            steps {{
                script {{
                    sonar_results = sh(script: 'sonar-scanner -Dsonar.projectKey={app_name} -Dsonar.sources=. -Dsonar.host.url={quality_tools}', returnStdout: true)
                    if (!sonar_results.contains('ANALYSIS SUCCESS')) {{
                        error 'Code quality check failed'
                    }}
                }}
            }}
        }}
        stage('Deploy') {{
            steps {{
                sh 'jfrog rt upload --url={file_repo} --user=admin --password=password target/{app_name}.war {file_repo}/{app_name}/'
            }}
        }}
    }}
    post {{
        always {{
            mail to: '{additional_inputs}',
                 subject: 'Pipeline completion notification for {app_name}({environment})',
                 body: "The pipeline has completed its execution. Please check the logs for any errors."
        }}
    }}
}}
    """
    print(pipeline_script)

if __name__ == '__main__':
    generate_pipeline()