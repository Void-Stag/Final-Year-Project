from flask import Blueprint, redirect, request, render_template, flash, url_for, session
from flask_login import login_user, logout_user, current_user, LoginManager
from run import db
from models import Task, User, Note
from auth.forms import UserLogin, CreateAccount, UserChangePassword
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

data = Blueprint('data', __name__, template_folder='templates')


#ToDo Tasks
@data.route('/Add_Task', methods=['POST'])
def addtask():
    id = session.get('user_id')
    if id is None:
        return redirect('/Login')
    taskname = request.form.get('taskname')
    duedate = datetime.fromisoformat(request.form.get('duedate'))
    if taskname!= '' and duedate !='' !=None:
        t = Task(taskname=taskname, duedate=duedate)
        db.session.add(t)
        db.session.commit()

    return redirect('/Home')

@data.route('/Delete_Task/<int:task_id>', methods=['GET', 'POST'])
def delete_task(task_id):
    id = session.get('user_id')
    if id is None:
        return redirect('/Login')
    if task_id:
        try:
            Task.query.filter(Task.id == task_id).delete()
            db.session.commit()
        except Exception as error:
            print(f"delete_task [{task_id}] Fail {error}")
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
            return redirect(url_for('data.Login'))
        if user:
            #print(f"login user 3")
            flash("You are now signed in!", "success")
            session['user_id'] = user.id
        return redirect('/Home')
    return render_template('Login and Accounts/login.html', title='Login', loginform=loginform)


@data.route('/Logout', methods=['GET','POST'])
def Logout():
    session.pop('user_id', None)
    flash("You've signed out!", "success")
    return redirect('/Login')

@data.route("/Change_Password", methods=["GET", "POST"])
def Change_Password():
    id = session.get('user_id')
    if id is None:
        return redirect('/Login')
    err_str = ""
    try:
        user = User.query.filter(User.id == id).one()
        passwordform = UserChangePassword()
        if user.check_password(passwordform.CurrentPassword.data):
            if passwordform.NewPassword.data == passwordform.NewPasswordRetype.data:
                user.password = generate_password_hash(passwordform.NewPassword.data)
                db.session.commit()
                return redirect('/Home')
            else:
                err_str = "New Password doesn't match"
                print(f"Check new password [{passwordform.NewPassword.data}] [{passwordform.NewPasswordRetype.data}]")
        else:
            print(f"Change Password db=[{user.password}] formpassword=[{passwordform.CurrentPassword.data}]")
            err_str = "Incorrect Password"
    except Exception as error:
        err_str = f"Account Settings unexpected error [{id}] Fail {error}"
    print(err_str)
    return render_template("Errors/error_page.html", title= err_str)

#Note Functions
@data.route('/Add_Note', methods=['POST'])
def Add_Note():
    id = session.get('user_id')
    if id is None:
        return redirect('/Login')
    title = request.form.get('title')
    content = request.form.get('content')
    #print(f"addnote {title} {content}")
    if title!= '' and content !='' !=None:
        n = Note(title=title, content=content)
        db.session.add(n)
        db.session.commit()
        flash('Note Created!', 'success')

    return redirect('/Home')


@data.route('/Delete_Note/<int:note_id>', methods=['GET', 'POST'])
def Delete_Note(note_id):
    id = session.get('user_id')
    if id is None:
        return redirect('/Login')
    if note_id:
        try:
            Note.query.filter(Note.id == note_id).delete()
            db.session.commit()
        except Exception as error:
         print(f"delete_note [{note_id}] Fail {error}")
    return redirect('/Home')


@data.route('/View_Note/<int:note_id>', methods= ['GET', 'POST'])
def View_Note(note_id):
    id = session.get('user_id')
    if id is None:
        return redirect('/Login')
    note = None
    if note_id:
        try:
            note = Note.query.filter(Note.id == note_id).one()
        except Exception as error:
            print(f"view_note [{note_id}] Fail {error}")
        """ Suggestion to redirect to an error page """
    return render_template('/Notes/view_note.html', title='View Note', note=note)


@data.route('/Edit_Note/<int:note_id>', methods= ['GET', 'POST'])
def Edit_Note(note_id):
    id = session.get('user_id')
    if id is None:
        return redirect('/Login')
    note = None
    if note_id:
        try:
            note = Note.query.filter(Note.id == note_id).one()
        except Exception as error:
            print(f"view_note [{note_id}] Fail {error}")
    #print(f"view_note [{id}] [{note}]")
    return render_template('/Notes/edit_note.html', title='Edit Note', note=note)


@data.route('/Update_Note/<int:note_id>', methods=['GET','POST'])
def Update_Note(note_id):
    id = session.get('user_id')
    if id is None:
        return redirect('/Login')
    #print(f"update_note 1 id = [{id}]")
    note = Note.query.filter(Note.id == note_id).one()
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
            print(f"update_note [{note_id}] Fail [{error}]")
