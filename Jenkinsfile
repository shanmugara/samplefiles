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
				step {
					echo 'Testing..'
				     }
                                step {
					cd section_1
				     }
				step {
                                	./helloworld.sh
				     }
			}
		}

		stage('Deploy') {
			steps {
				echo 'Deploying....'
			}
		}

	}
}

