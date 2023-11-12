from app import NoteA, db
from routes import *
from models import *
from databaseroutes import *
from auth.forms import *
from flask_login import LoginManager

NoteA.register_blueprint(web)
NoteA.register_blueprint(data)

def create_app():

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(NoteA)

    db.init_app(NoteA)

    with NoteA.app_context():
        db.create_all()
    return NoteA



