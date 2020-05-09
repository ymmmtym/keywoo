from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def get_toppage(str):
    list = str.split('/')
    return list[0] + '//' + list[2]

app = Flask(__name__)
app.config.from_object('keywoo.config')
app.jinja_env.globals['get_toppage'] = get_toppage

db = SQLAlchemy(app)

import keywoo.views