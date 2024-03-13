from app import db
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.orm import backref
from werkzeug.security import generate_password_hash, check_password_hash


class TimestampMixin(object):
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    taskname = db.Column(db.String(75))
    duedate = db.Column(db.DateTime)
    """ User_id Foreign Key """
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_task = db.relationship("User",backref=backref("user_task", uselist=False) )

    def __init__(self, taskname, duedate, user_id):
        self.taskname = taskname
        self.duedate = duedate
        self.user_id = user_id

    def __repr__(self):
        return f"<Task {self.taskname}>"


class User(db.Model, UserMixin, TimestampMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(20))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<Task {self.username}>"

    # check user password is correct
    def check_password(self, password):
        print(f"check_password 1 [{self.password}] [{password}]")
        return check_password_hash(self.password, password)


class Note(db.Model, TimestampMixin):
    __tablename__ = 'note'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(10000))
    """ User_id Foreign Key """
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_note = db.relationship("User",backref=backref("user_note", uselist=False) )

    """ contentsnip takes the note content data from the database and shortens it for main page display """
    @ property
    def contentsnip(self):
        return self.content[:10]

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f"<Task {self.title}>"
