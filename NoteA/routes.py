from flask import Blueprint, render_template, session, redirect
from models import Task, Note, User
from auth.forms import UserChangePassword

web = Blueprint("web", __name__, template_folder="templates")


@web.route("/Home", methods=["GET", "POST"])
def Home():
    id = session.get('user_id')
    if id is None:
        return redirect('/Login')
    """ Content is filtered by current user id in session which matches items in database. """
    tasks = Task.query.filter(Task.user_id == id)
    notes = Note.query.filter(Note.user_id == id)
    return render_template("Main/main_page.html", title="Home", tasks=tasks, notes=notes)

@web.route("/Account_Settings", methods=["GET", "POST"])
def Account_Settings():
    passwordform = UserChangePassword()
    return render_template("Login and Accounts/Account/settings.html", title="Settings", passwordform=passwordform)


@web.route("/Create_Note", methods=["GET", "POST"])
def Create_Note():
    return render_template("Notes/create_note.html", title="Create Note")
