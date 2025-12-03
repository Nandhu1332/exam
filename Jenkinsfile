pipeline{
    agent any
    stages{
      stage('Build Docker Inage'){
        steps{
          echo "Build Docker Image"
          bat "docker build -t myapp:v1 ."
        }
      }
      stage('Dokcer Login'){
        steps{
            bat "docker login -u kadarinandhini -p admin@123"
        }
      }
      stage('push Docker Image to Docker Hub'){
        steps{
            echo "push Docker Image to Docker Hub"
            bat "docker tag myapp:v1 kadarinandhini/sample:t1"
            bat "docker push kadarinandhini/sample:t1"
        }
      }
      stage('Deploy to kubernetes'){
        steps{
            bat "kubectl apply -f deployment.yaml --validate=false"
            bat "kubectl apply -f service.yaml"
        }
      }
    }
    post{
        success{
            echo 'Pipeline completed successfully!'
        }
        failure{
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}