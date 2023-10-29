from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    taskname = db.Column(db.String(75))
    duedate = db.Column(db.DateTime)

    def __init__(self, taskname, duedate):
        self.taskname = taskname
        self.duedate = duedate

    def __repr__(self):
        return f'<Task {self.taskname}>'