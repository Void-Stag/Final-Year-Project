from app import db
from datetime import datetime
from flask_login import UserMixin

class TimestampMixin(object):
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    taskname = db.Column(db.String(75))
    duedate = db.Column(db.DateTime)

    def __init__(self, taskname, duedate):
        self.taskname = taskname
        self.duedate = duedate

    def __repr__(self):
        return f'<Task {self.taskname}>'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(20))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<Task {self.username}>'

class Note(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(10000))