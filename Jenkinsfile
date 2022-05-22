pipeline{
    agent any
    stages{
        stage('Clone Repo From GitHub'){
            steps{
                script{
                    if(fileExists('/home/jenkins/.jenkins/workspace/QA-practical-assessment')){
                        sh 'cd QA-practical-assessment && git pull'
                    }
                    else{
                        sh 'https://github.com/karljay98/QA-practical-assessment.git'
                    }
                }
            }
        }
        stage('Requirements Installations'){
            steps{
                sh 'cd QA-practical-assessment && pip3 install -r s1/application/requirements.txt'
                sh 'cd QA-practical-assessment && pip3 install -r s2/application/requirements.txt'
                sh 'cd QA-practical-assessment && pip3 install -r s3/application/requirements.txt'
                sh 'cd QA-practical-assessment && pip3 install -r s4/application/requirements.txt'
            }
        }
        stage('Mock Testing'){
            steps{
                sh 'cd QA-practical-assessment/s1 && python3 -m pytest --cov=application'
                sh 'cd QA-practical-assessment/s2 && python3 -m pytest --cov=application'
                sh 'cd QA-practical-assessment/s3 && python3 -m pytest --cov=application'
                sh 'cd QA-practical-assessment/s4 && python3 -m pytest --cov=application'
            }
        }
        stage('Building Application and Pushing Images to DockerHub'){
            steps{
                sh 'cd QA-practical-assessment && docker-compose build'
                sh 'cd QA-practical-assessment && docker-compose push'
            }
        }
        stage('Deployment of Application'){
            steps{
                sh 'cd QA-practical-assessment && docker-compose up -d'
            }
        }
    }
}