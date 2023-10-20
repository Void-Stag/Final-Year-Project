import jwt
from time import time
from app import db, login
from datetime import datetime
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class TimestampMixin(object):
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)


class User(db.Model, TimestampMixin, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))


    # print to console username created
    def __repr__(self):
        return f'<User {self.username}>'
    # generate user password i.e. hashing
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    # check user password is correct
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    # for reseting a user password
    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'],
            algorithm='HS256').decode('utf-8')
    # verify token generated for resetting password
    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

