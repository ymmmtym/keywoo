from keywoo import db


class InitDB:
    "create database"

    def run(self):
        db.create_all()


class DropDB:
    "drop database"

    def run(self):
        db.drop_all()