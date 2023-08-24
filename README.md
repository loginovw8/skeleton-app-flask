# Flask

## Steps to install and run

Fill credentials in scripts/venv.sh

	Look scripts/venv.sh.example for pattern

Create an environment

	python3 -m venv venv

Activate the environment 	

	. venv/bin/activate

Activate the environemnt with script 

	source scripts/venv.sh

Install Flask

	pip install Flask pymysql python-dotenv

Secure the sessions that remember information from one request to another

	export SECRET_KEY='Z#fg%kolL3'

Set a database URI

	export DATABASE_URI='mysql+pymysql://root:secret@localhost/talant'

Define path for the create_app() factory function

	export FLASK_APP=app

Run the application

	flask run

Alternative way is to use script

	sh scripts/run.sh

## Interactive console

Open Flask Shell

	flask shell

Alternative way is to use script

	sh scripts/shell.sh

Deactivate the environment

	deactivate
