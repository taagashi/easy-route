#!/bin/bash
cd easy_route

set -e

python manage.py migrate
python manage.py collectstatic --noinput

exec gunicorn easy_route.wsgi:application --bind 0.0.0.0:$PORT