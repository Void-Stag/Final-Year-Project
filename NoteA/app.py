from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

NoteA = Flask(__name__)
NoteA.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///website.db'

db = SQLAlchemy(NoteA)
migrate = Migrate(NoteA, db)