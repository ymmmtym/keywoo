import click
from keywoo import app
from keywoo.scripts.db import InitDB


@click.group()
def manager():
    pass


@manager.command("init_db")
def init_db():
    with app.app_context():
        InitDB().run()


if __name__ == "__main__":
    manager()
