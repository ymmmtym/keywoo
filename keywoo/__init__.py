from flask import Flask


def get_toppage(str):
    list = str.split('/')
    return list[0] + '//' + list[2]

app = Flask(__name__)
app.config.from_object('keywoo.config')
app.jinja_env.globals['get_toppage'] = get_toppage

import keywoo.views