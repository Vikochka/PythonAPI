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
           // To run Maven on a Windows agent, use
           bat "python -m pytest --alluredir results"
  }
  post('Reports') {
    always{
    script {
             allure([
                     includeProperties: false,
                     jdk: '',
                     properties: [],
                     reportBuildPolicy: 'ALWAYS',
                     results: [[path: 'allureresults']]
             ])
     }
    }
  }
}