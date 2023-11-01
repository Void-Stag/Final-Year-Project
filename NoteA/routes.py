from flask import Blueprint, render_template
from models import Task

web = Blueprint('web', __name__, template_folder='templates')



@web.route('/')
@web.route('/login', methods=['GET','POST'])
def login(cat=None):
    return render_template('Login/login.html', title='Login')


@web.route('/home', methods=['GET','POST'])
def home(cat=None):
    tasks = Task.query.all()
    return render_template('homepage.html', title='Home' ,tasks=tasks)

@web.route('/createaccount', methods=['GET','POST'])
def createaccount(cat=None):
    return render_template('Login/createacc.html', title='Create Account')

