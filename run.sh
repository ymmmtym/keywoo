#!/bin/sh

python manage.py init_db
uwsgi --ini uwsgi.ini