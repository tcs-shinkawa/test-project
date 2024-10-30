#!/bin/bash
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
gunicorn test_prj.wsgi:application --bind 0.0.0.0:8000
