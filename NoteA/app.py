import os
import yaml #Importing a file format for app config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def read_config(appconfig):
    if os.path.isfile(appconfig):
        with open(appconfig, 'r', encoding="utf-8") as config_file:
            return yaml.safe_load(config_file)
    return {}

NoteA_config = read_config('NoteA_config.yaml')

NoteA = Flask(__name__)
NoteA.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///website.db'
NoteA.config ['SECRET_KEY'] = NoteA_config['NoteA']['security']['key']




db = SQLAlchemy(NoteA)
migrate = Migrate(NoteA, db)