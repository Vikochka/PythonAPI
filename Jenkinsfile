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
           bat "python -m pytest -rP test --alluredir allure-report"
  }

 stage('Report') {
            bat "allure generate allure-report --clean -o allure-report || true && allure report open -o allure-report"
             script {
                     allure([
                             includeProperties: false,
                             jdk: '',
                             properties: [],
                             reportBuildPolicy: 'ALWAYS',
                             results: [[path: '../allure-results']]
                     ])
             }

 }
}