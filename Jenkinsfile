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
                                  cd section_1
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
