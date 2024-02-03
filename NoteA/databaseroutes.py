from flask import Blueprint, redirect, request, render_template, flash, url_for
from flask_login import login_user, logout_user, current_user, LoginManager
from run import db
from models import Task, User, Note
from auth.forms import UserLogin, CreateAccount
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

data = Blueprint('data', __name__, template_folder='templates')


#ToDo Tasks
@data.route('/Add_Task', methods=['POST'])
def addtask():
    taskname = request.form.get('taskname')
    duedate = datetime.fromisoformat(request.form.get('duedate'))
    if taskname!= '' and duedate !='' !=None:
        t = Task(taskname=taskname, duedate=duedate)
        db.session.add(t)
        db.session.commit()

    return redirect('/Home')


@data.route('/Delete_Task/<int:id>', methods=['GET', 'POST'])
def delete_task(id):
    if id:
        try:
            Task.query.filter(Task.id == id).delete()
            db.session.commit()
        except Exception as error:
            print(f"delete_task [{id}] Fail {error}")
    return redirect('/Home')


#User Account & Login
@data.route('/Create_Account', methods=['GET', 'POST'])
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
        return redirect('/Login')
    return render_template('Login and Accounts/create_account.html', title='Create Account', accform=accform)


#Login and User Account Authentication
@data.route('/')
@data.route('/Login', methods=['GET', 'POST'])
def Login():
    loginform = UserLogin()
    if loginform.validate_on_submit():
        #print(f"login user 1")
        user = User.query.filter_by(username=loginform.Username.data.strip()).first()
        #print(f"login user [{user.username}] [{user.password}] [{user}]")
        if not user.check_password(loginform.Password.data):
            #print(f"login user 2")
            flash('Invalid username or password', 'danger')
            return redirect(url_for('data.login'))
        if user:
            #print(f"login user 3")
            flash("You are now signed in!", "success")
        return redirect('/Home')
    return render_template('Login and Accounts/login.html', title='Login', loginform=loginform)


@data.route('/Logout', methods=['GET','POST'])
def Logout():
    logout_user()
    flash("You've signed out!", "success")
    return redirect('/Login')

@data.route('/Update_Password', methods=['GET', 'POST'])
def Update_Password():

    return redirect('/Account_Settings')

#Note Functions
@data.route('/Add_Note', methods=['POST'])
def Add_Note():
    title = request.form.get('title')
    content = request.form.get('content')
    #print(f"addnote {title} {content}")
    if title!= '' and content !='' !=None:
        n = Note(title=title, content=content)
        db.session.add(n)
        db.session.commit()
        flash('Note Created!', 'success')

    return redirect('/Home')


@data.route('/Delete_Note/<int:id>', methods=['GET', 'POST'])
def Delete_Note(id):
    if id:
        try:
            Note.query.filter(Note.id == id).delete()
            db.session.commit()
        except Exception as error:
         print(f"delete_note [{id}] Fail {error}")
    return redirect('/Home')


@data.route('/View_Note/<int:id>', methods= ['GET', 'POST'])
def View_Note(id):
    note = None
    if id:
        try:
            note = Note.query.filter(Note.id == id).one()
        except Exception as error:
            print(f"view_note [{id}] Fail {error}")
        """ Suggestion to redirect to an error page """
    return render_template('/Notes/view_note.html', title='View Note', note=note)


@data.route('/Edit_Note/<int:id>', methods= ['GET', 'POST'])
def Edit_Note(id):
    note = None
    if id:
        try:
            note = Note.query.filter(Note.id == id).one()
        except Exception as error:
            print(f"view_note [{id}] Fail {error}")
    #print(f"view_note [{id}] [{note}]")
    return render_template('/Notes/edit_note.html', title='Edit Note', note=note)


@data.route('/Update_Note/<int:id>', methods=['GET','POST'])
def Update_Note(id):
    #print(f"update_note 1 id = [{id}]")
    note = Note.query.filter(Note.id == id).one()
    #print(f"update_note 2 id = [{id}]")
    if note:
        #print(f"update_note 3 id = [{id}]")
        try:
            #print(f"update_note 4 id = [{id}]")
            title = request.form.get('title')
            content = request.form.get('content')
            #print(f"update_note 5 [{title}] [{content}]")
            note.title = title
            note.content = content
            #print(f"update_note 6 id = [{id}]")
            db.session.commit()
            return render_template('/Notes/view_note.html', title='View Note', note=note)
        except Exception as error:
            print(f"update_note [{id}] Fail [{error}]")
