pipeline {
    agent any
    stages {
        stage('Generate Docs') {
            steps {
                sh 'echo $PATH'
                sh 'chmod -R 755 .'
                sh 'sudo pip3.8 install jinja2 requests'
                sh '/usr/local/bin/python3.8 --version'
                sh '/usr/local/bin/python3.8 ./create_docs.py'
            }
        }
        stage('Commit Docs') {
            steps {
                echo 'Commit Docs'
            }
        }
        stage('Function Tests') {
            steps {
                echo 'Run Tests'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
        success {
            echo 'successful'
        }
        failure {
            echo 'failed'
        }
        unstable {
            echo 'unstable'
        }
        changed {
            echo 'changed'
        }
    }
}

