from flask import Blueprint, render_template
from models import Task, Note, User
from auth.forms import UserChangePassword

web = Blueprint("web", __name__, template_folder="templates")


@web.route("/Home", methods=["GET", "POST"])
def Home():
    tasks = Task.query.all()
    notes = Note.query.all()
    user = User.query.all()
    return render_template("Main/main_page.html", title="Home", tasks=tasks, notes=notes, user=user)

@web.route("/Account_Settings", methods=["GET", "POST"])
def Account_Settings():
    passwordform = UserChangePassword()
    return render_template("Login and Accounts/Account/settings.html", title="Settings", passwordform=passwordform)


@web.route("/Create_Note", methods=["GET", "POST"])
def Create_Note():
    return render_template("Notes/create_note.html", title="Create Note")
