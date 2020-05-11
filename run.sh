#!/bin/sh

python manage.py init_db
uwsgi --http=0.0.0.0:5000 --wsgi-file=${APP}/run.py  --callable=app
# flask run -h 0.0.0.0