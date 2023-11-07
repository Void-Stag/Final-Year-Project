from app import NoteA, db
from routes import *
from models import *
from databaseroutes import *
from auth.forms import *

NoteA.register_blueprint(web)
NoteA.register_blueprint(data)

def create_app():

    db.init_app(NoteA)

    with NoteA.app_context():
        db.create_all()
    return NoteA



