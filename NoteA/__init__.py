from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes import main
from NoteA.auth.routes import auth
db = SQLAlchemy()


def create_app():
    NoteA = Flask(__name__)
    NoteA.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///website.db'

    db.init_app(NoteA)
    NoteA.register_blueprint(main)
    NoteA.register_blueprint(auth)

    with NoteA.app_context():
        db.create_all()
    return NoteA

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    taskname = db.Column(db.String(75))
    duedate = db.Column(db.DateTime)

    def __init__(self, taskname, duedate):
        self.taskname = taskname
        self.duedate = duedate

    def __repr__(self):
        return f'<Task {self.taskname}>'