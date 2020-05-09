from flask_script import Manager
from keywoo import app

from keywoo.scripts.db import InitDB


if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command('init_db', InitDB())
    # manager.add_command('drop_db', DrpoDB())
    manager.run()