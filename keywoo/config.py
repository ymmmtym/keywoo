import os

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "sqlite:///keywoo.db"
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG=True
THREADED = True
TESTING=True
JSON_AS_ASCII = False
SECRET_KEY = os.urandom(12)