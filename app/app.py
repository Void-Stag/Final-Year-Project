import os, secrets
import logging
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask_login import LoginManager
from flask import render_template,request
from routes import main

#db = SQLAlchemy()
migrate = Migrate()
SECRET_KEY = os.environ.get('SECRET_KEY')
app = Flask(__name__)


#db.init_app(app)
#migrate.init_app(app, db)

#Importing blueprints


app.register_blueprint(main)




