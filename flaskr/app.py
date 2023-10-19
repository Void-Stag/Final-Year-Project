import os

from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def home(cat=None):
    return render_template('base.html', title='Home')
