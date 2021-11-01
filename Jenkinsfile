pipeline {
    agent any
    stages {
        stage('Scan') {
            steps {
              def scannerHome ='C://Install//sonarqube-9.1.0.47736//sonarqube-9.1.0.47736//bin'
              withSonarQubeEnv(installationName:'sonarqube')
                sh '${scannerHome}/bin/sonar-scanner:scanner'
            }
        }
    }
}