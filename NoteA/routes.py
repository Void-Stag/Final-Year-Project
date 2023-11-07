from flask import Blueprint, render_template
from models import Task

web = Blueprint('web', __name__, template_folder='templates')


@web.route('/home', methods=['GET','POST'])
def home(cat=None):
    tasks = Task.query.all()
    return render_template('homepage.html', title='Home' ,tasks=tasks)

