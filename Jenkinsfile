pipeline {

    agent any

    environment {
        IMAGE_NAME = 'cloudlab-flask'
    }

    stages {

        stage('Checkout Source') {
            steps {
                git(
                    branch: 'main',
                    url: 'https://github.com/your-username/your-cloudlab-project.git'
                )
            }
        }

        stage('Create Container Image') {
            steps {
                sh '''
                    echo "Building Flask application image..."
                    docker build -t ${IMAGE_NAME}:latest .
                '''
            }
        }

        stage('Refresh Application') {
            steps {
                sh '''
                    echo "Stopping previous deployment..."
                    docker compose down || true

                    echo "Starting updated services..."
                    docker compose up -d --build
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    echo "Checking running containers..."
                    docker compose ps
                '''
            }
        }
    }

    post {
        success {
            echo 'CloudLab deployment completed successfully.'
        }

        failure {
            echo 'Deployment failed. Check the Jenkins console output.'
        }
    }
}