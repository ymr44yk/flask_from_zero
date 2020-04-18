from flask_script import Command
from flask_blog import db

class InitDB(Command):
    "crete database"

    def run(self):
        db.create_all()

class DropDB(Command):
    "drop database"

    def run(self):
        db.drop_all()
                