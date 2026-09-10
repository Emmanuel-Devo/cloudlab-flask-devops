pipeline {

```
agent any

environment {
    IMAGE_NAME = 'cloudlab-flask'
}

stages {

    stage('Checkout Source') {
        steps {
            git(
                branch: 'main',
                url: 'https://github.com/Emmanuel-Devo/cloudlab-flask-devops.git'
            )
        }
    }

    stage('Create Container Image') {
        steps {
            bat '''
                echo Building Flask application image...
                docker build -t %IMAGE_NAME%:latest .
            '''
        }
    }

    stage('Refresh Application') {
        steps {
            bat '''
                echo Stopping previous deployment...
                docker compose down

                echo Starting updated services...
                docker compose up -d --build
            '''
        }
    }

    stage('Verify Deployment') {
        steps {
            bat '''
                echo Checking running containers...
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
```

}
