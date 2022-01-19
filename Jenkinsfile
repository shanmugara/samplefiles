#!/usr/bin/groovy
// Declarative Pipeline
pipeline {
	agent lnxmaster

	stages {

		stage('Build') {
			steps {
				echo 'Building..'
			}
		}

		stage('Test') {
			steps {
			       sh "echo 'Testing..'"
			       sh '''
                                  cd section_1
                                  ./helloworld.sh
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
