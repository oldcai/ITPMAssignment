#!/bin/bash
GUNICORN_LOG_LEVEL=${LOG_LEVEL:-DEBUG}
python manage.py collectstatic --noinput &
mkdir -p /code/db
mkdir -p /mnt/static
python manage.py migrate --noinput
gunicorn -c gunicorn.py itpm.wsgi --log-level=$GUNICORN_LOG_LEVEL
