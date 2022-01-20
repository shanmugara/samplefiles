#!/usr/bin/groovy
// Declarative Pipeline
pipeline {
	agent {label 'winnode2'}

	stages {

		stage('Update_nl') {
			steps {
			       bat "echo 'Updating named locations..'"
			       bat '''
                                  C:\\Python\\venv\\azgraph\\Scripts\\callgraph.exe nlconf -u -f nl_files/omegamsdn_nl_my_isp.csv 
                               '''
		}
                }

	}
}
