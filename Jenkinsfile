pipeline {
  agent {
    docker {
      image 'ubuntu:16.04'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh '''./bootstrap.sh
./build.sh'''
      }
    }
  }
}
