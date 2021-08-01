pipeline { 
    agent any 
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') { 
            steps { 
                sh 'pip3 install -r req.txt'
            }
        }
        stage('Test'){
            steps {
               sh 'python3 manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo deploying'
            }
        }
           
        stage('Ok') {
            steps {
                echo "Ok"
            }
        }
    
    post {
        always {
            emailext body: 'A Test EMail', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
        }
    }
    }
}
