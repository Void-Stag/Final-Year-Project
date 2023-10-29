from flask import Blueprint, redirect, request
from run import db
from models import Task
from flask import jsonify
from datetime import datetime
data = Blueprint('data', __name__, template_folder='templates')

#ToDo Tasks
@data.route('/addtask', methods=['POST'])
def addtask():
    taskname = request.form.get('taskname')
    duedate = datetime.strptime(request.form.get('duedate'), '%d/%m/%Y')
    print(f"{request.form}")
    print(f"addtask 1: {taskname} {duedate}")
    if taskname!= '' and duedate !='' !=None:
        t = Task(taskname=taskname, duedate=duedate)
        db.session.add(t)
        db.session.commit()

    return redirect('/home')

@data.route('/showtask', methods=['GET','POST'])
def showtask():
    task = []
    for row in Task.query.all():
        task.append((str(row.taskname), str(row.duedate)))
        print(f"showtask {task}")
    return jsonify(task)