from flask import Blueprint, redirect, request, render_template, flash, url_for
from flask_login import login_user
from run import db
from models import Task, User, Note
from auth.forms import UserLogin, CreateAccount
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

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
    if accform.validate_on_submit():

        password_hash = generate_password_hash(accform.Password.data)

        user = User(
            username = accform.Username.data,
            password = password_hash
        )
        db.session.add(user)
        db.session.commit()
        flash('Account Created!', 'success')
        return redirect('/login')
    return render_template('Login/createacc.html', title='Create Account', accform=accform)

#Login and User Account Authentication
@data.route('/')
@data.route('/login', methods=['GET', 'POST'])
def login():
    loginform = UserLogin()
    if loginform.validate_on_submit():
        print(f"login user 1")
        user = User.query.filter_by(username=loginform.Username.data.strip()).first()
        print(f"login user [{user.username}] [{user.password}] [{user}]")
        if not user.check_password(loginform.Password.data):
            print(f"login user 2")
            flash('Invalid username or password', 'danger')
            return redirect(url_for('data.login'))
        if user:
            print(f"login user 3")
            flash("You are now signed in!", "success")
        return redirect('/home')
    return render_template('Login/login.html', title='Login', loginform=loginform)

@data.route('/logout', methods=['GET','POST'])

#Notes
@data.route('/addnote', methods=['POST'])
def addnote():
    title = request.form.get('title')
    content = request.form.get('content')
    #print(f"addnote {title} {content}")
    if title!= '' and content !='' !=None:
        n = Note(title=title, content=content)
        db.session.add(n)
        db.session.commit()
        flash('Note Created!', 'success')

    return redirect('/home')

@data.route('/delete_note/<int:id>', methods=['GET', 'POST'])
def delete_note(id):
    if id:
        try:
            Note.query.filter(Note.id == id).delete()
            db.session.commit()
        except Exception as error:
            print(f"delete_note [{id}] Fail {error}")
    return redirect('/home')
