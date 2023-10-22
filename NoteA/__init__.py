import os
from flask import Flask
from .routes import main
#from .auth import routes.auth


NoteA = Flask(__name__)
NoteA.debug = True

#Importing blueprints
NoteA.register_blueprint(main)
#NoteA.register_blueprint(routes.auth)