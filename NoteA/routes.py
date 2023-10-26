from flask import Blueprint, render_template, redirect, url_for, request
from flask import jsonify

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
@main.route('/login', methods=['GET','POST'])
def login(cat=None):
    return render_template('Login/login.html', title='Login')


@main.route('/home', methods=['GET','POST'])
def home(cat=None):
    return render_template('homepage.html', title='Home')

@main.route('/createaccount', methods=['GET','POST'])
def createaccount(cat=None):
    return render_template('Login/createacc.html', title='Create Account')

