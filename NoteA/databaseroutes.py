from flask import Blueprint, redirect, request
from run import db
from models import Task
from flask import jsonify

data = Blueprint('data', __name__, template_folder='templates')

#ToDo Tasks
@data.route('/addtask', methods=['POST'])
def addtask():
    task = request.form.get('taskname')
    date = request.form.get('duedate')

    if task!= '' and date !='' !=None:
        t = Task(taskname=task, duedate=date)
        db.session.add(t)
        db.session.commit()

    redirect('/home')

@data.route('/showtask', methods=['GET','POST'])
def showtask():
    task = []
    for row in Task.query.all():
        task.append((str(row.task), str(row.date)))
    return jsonify(task)