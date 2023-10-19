from flask import Blueprint, render_template, redirect, url_for, request
from app.models import db
from flask import jsonify

main = Blueprint('main', __name__)
