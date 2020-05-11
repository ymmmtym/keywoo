import os

SQLALCHEMY_DATABASE_URI = "postgresql://keywoo:keywoo@db:5432/keywoo"
SQLALCHEMY_TRACK_MODIFICATIONS = True
ENV = 'production'
THREADED = True
JSON_AS_ASCII = False
SECRET_KEY = os.urandom(12)
