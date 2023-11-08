from flask import Blueprint, redirect, request, render_template
from run import db
from models import Task, User
from auth.forms import UserLogin, CreateAccount
from datetime import datetime
data = Blueprint('data', __name__, template_folder='templates')


#ToDo Tasks
@data.route('/addtask', methods=['POST'])
def addtask():
    taskname = request.form.get('taskname')
    duedate = datetime.fromisoformat(request.form.get('duedate'))
    if taskname!= '' and duedate !='' !=None:
        t = Task(taskname=taskname, duedate=duedate)
        db.session.add(t)
        db.session.commit()

    return redirect('/home')

@data.route('/delete_task/<int:id>', methods=['GET', 'POST'])
def delete_task(id):
    if id:
        try:
            Task.query.filter(Task.id == id).delete()
            db.session.commit()
        except Exception as error:
            print(f"delete_task [{id}] Fail {error}")
    return redirect('/home')

#User Account & Login
@data.route('/CreateAccount', methods=['GET', 'POST'])
def CreateAccountRoot():
    accform = CreateAccount()
    return render_template('Login/createacc.html', title='Create Account', accform=accform)

@data.route('/')
@data.route('/login', methods=['GET', 'POST'])
def login():
    loginform = UserLogin()
    return render_template('Login/login.html', title='Login', loginform=loginform)
