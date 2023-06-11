#!/bin/sh
export FLASK_APP=./Backend-CRUD-App/app.py
pipenv run flask --debug run -h 0.0.0.0
