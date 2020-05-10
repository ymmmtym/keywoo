import os

SQLALCHEMY_DATABASE_URI = "postgresql://keywoo:keywoo@db:5432/keywoo"
# SQLALCHEMY_DATABASE_URI = "sqlite:///keywoo.db" # local
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG=True
THREADED = True
TESTING=True
JSON_AS_ASCII = False
SECRET_KEY = os.urandom(12)