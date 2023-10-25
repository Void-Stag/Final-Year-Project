from flask import Blueprint, render_template, redirect, url_for, request
from NoteA.__init__ import db,Task
from flask import jsonify

auth = Blueprint('auth', __name__, template_folder='templates')

#ToDo Tasks
@auth.route('/addtask', methods=['POST'])
def addtask():
    task = request.form.get('taskname')
    date = request.form.get('duedate')

    if task!= '' and date !='' !=None:
        p = Task(taskname=task, duedate=date)
        db.session.add(p)
        db.session.commit()

    redirect('/home')