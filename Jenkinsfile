#!/usr/bin/groovy
// Declarative Pipeline
pipeline {
	agent any

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
                                  ./helloword.sh
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
