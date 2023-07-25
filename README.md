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

	pip install Flask Flask-SQLAlchemy bs4 flask-login flask_migrate requests pymysql flask-wtf faker cryptography uwsgi email_validator pillow python-dotenv pandas openpyxl xlsxwriter xlrd

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

Receive the URI path to your database (in shell mode)

	>>> from app.extensions import db
	>>> print(db)

## Database migrations

Initialize migrations

	flask db init

Autogenerate a new revision file

	flask db migrate

Upgrade to a later version

	flask db upgrade

Revert to a previous version

	flask db downgrade

Generate school tokens (in shell mode)

	>>> from scripts.parse_schools import start_parse
	>>> start_parse()

Generate default statuses (in shell mode)

	>>> from scripts.add_defaultstatus import add_default
	>>> add_default()

Deactivate the environment

	deactivate

Deployment

	https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-20-04
