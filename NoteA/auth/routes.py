from flask import Blueprint, render_template, redirect, url_for, request
#from app.models import db,ToDo
from flask import jsonify

auth = Blueprint('auth', __name__, template_folder='templates')

#ToDo Tasks
#@auth.route('/addtask', methods=['POST'])
#def addtask():
#    task