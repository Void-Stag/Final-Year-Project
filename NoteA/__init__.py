from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from NoteA import routes#, authroutes
from flask_migrate import Migrate

NoteA = Flask(__name__)
NoteA.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///website.db'

db = SQLAlchemy(NoteA)
migrate = Migrate(NoteA, db)

NoteA.register_blueprint(routes.main)

#NoteA.register_blueprint(authroutes.auth)

NoteA.register_blueprint(Blueprint('auth', __name__, template_folder='templates'))
def create_app():
   # NoteA = Flask(__name__)
    NoteA.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///website.db'

    db.init_app(NoteA)



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