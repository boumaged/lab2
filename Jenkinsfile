pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/boumaged/lab2.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover'
            }
        }
    }
}

