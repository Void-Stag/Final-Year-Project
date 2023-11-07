from flask import Blueprint, render_template
from models import Task

web = Blueprint('web', __name__, template_folder='templates')


@web.route('/Home', methods=['GET','POST'])
def home():
    tasks = Task.query.all()
    return render_template('homepage.html', title='Home' ,tasks=tasks)

@web.route('/AccountSettings', methods=['GET', 'POST'])
def AccountSettings():
    return render_template('Account/settings.html', title='Settings')
