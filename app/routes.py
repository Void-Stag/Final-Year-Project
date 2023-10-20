from flask import Blueprint, render_template, redirect, url_for, request
#from app.models import db
from flask import jsonify

main = Blueprint('main', __name__, template_folder='templates')


def login(cat=None):
    return render_template('Login/login.html', title='Login')

@main.route('/')
@main.route('/Home', methods=['GET','POST'])
def home(cat=None):
    return render_template('homepage.html', title='Home')

