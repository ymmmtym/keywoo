from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


def get_toppage(str):
    list = str.split('/')
    return list[0] + '//' + list[2]

app = Flask(__name__)
app.config.from_object('keywoo.config')
app.jinja_env.globals['get_toppage'] = get_toppage

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

from keywoo.models.users import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

import keywoo.views