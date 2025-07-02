pipeline {
    agent any

    environment {
        // Replace with your Jenkins GitHub credentials ID
        GITHUB_CREDENTIALS = 'github-creds'
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: "${GITHUB_CREDENTIALS}", url: 'https://github.com/your-username/your-repo.git', branch: 'main'
            }
        }
        stage('Install dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r messaging_app/requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest messaging_app/chats/tests.py --junitxml=report.xml
                '''
            }
        }
        stage('Publish Report') {
            steps {
                junit 'report.xml'
            }
        }
    }
    triggers {
        // No triggers: manual run only
    }
}
