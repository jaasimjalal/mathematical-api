pipeline {
    agent any
    
    environment {
        APP_NAME = 'mathematical-api'
        CONTAINER_NAME = 'mathematical-api-container'
        IMAGE_NAME = 'mathematical-api'
        PORT = '3000'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out repository...'
                checkout scm
            }
        }
        
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh 'python3 --version'
                sh 'pip3 install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Running automated tests...'
                sh 'python3 -m pytest tests/ -v --tb=short'
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh "docker build -t ${IMAGE_NAME}:latest ."
                sh "docker tag ${IMAGE_NAME}:latest ${IMAGE_NAME}:\${BUILD_NUMBER}"
            }
        }
        
        stage('Run Container') {
            steps {
                echo 'Stopping existing container...'
                sh "docker rm -f ${CONTAINER_NAME} || true"
                
                echo 'Starting new container...'
                sh "docker run -d --name ${CONTAINER_NAME} -p ${PORT}:3000 ${IMAGE_NAME}:latest"
                
                echo 'Waiting for service to be ready...'
                sh 'sleep 5'
                
                echo 'Health check...'
                sh "curl -f http://localhost:${PORT}/health || exit 1"
            }
        }
        
        stage('Integration Test') {
            steps {
                echo 'Running integration tests against running container...'
                script {
                    def operations = ['add', 'subtract', 'multiply', 'divide', 'power', 'sqrt', 'sin', 'cos', 'tan']
                    operations.each { op ->
                        sh "curl -s -X POST http://localhost:${PORT}/api/v1/${op} -H 'Content-Type: application/json' -d '{}' || echo 'Testing ${op}'"
                    }
                }
            }
        }
        
        stage('Cleanup') {
            steps {
                echo 'Cleaning up containers...'
                sh "docker rm -f ${CONTAINER_NAME} || true"
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
    }
}