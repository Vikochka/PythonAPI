node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SONAR_RUNNER_HOME';
        withSonarQubeEnv() {
        bat "${scannerHome}/bin/sonar-scanner"
    }
  }

  stage('Build') {
           git 'https://github.com/Vikochka/PythonAPI.git'
           bat "python -m pytest -k test --alluredir results"
  }

 stage('Report') {
            bat "allure --clean report"
            bat "allure generate results -o report"
             script {
                     allure([
                             includeProperties: false,
                             jdk: '',
                             properties: [],
                             reportBuildPolicy: 'ALWAYS',
                             results: [[path: '../report']]
                     ])
             }

 }
}