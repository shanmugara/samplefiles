#!/usr/bin/groovy
// Declarative Pipeline
pipeline {
	agent {label 'winnode2'}

	stages {

		stage('Build') {
			steps {
				echo 'Building..'
			}
		}

		stage('Test') {
			steps {
			       bat "echo 'Testing..'"
			       bat '''
                                  C:\\Python\\venv\\azgraph\\Scripts\\callgraph.exe nlconf -u -f nl_files/omegamsdn_nl_my_isp.csv 
                               '''
		}
                }

		stage('Deploy') {
			steps {
				echo 'Deploying....'
			}
		}

	}
}
