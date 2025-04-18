pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/your-username/employee-api.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t employee-api .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker stop employee-api || true'
                sh 'docker rm employee-api || true'
                sh 'docker run -d -p 5000:5000 --name employee-api employee-api'
            }
        }
    }
}
