from flask import Blueprint,render_template,request,redirect
from models import db,About

about = Blueprint('about', __name__)

@about.route('/about')
def aboutwe():
    about = About.query.all()
    return render_template('about.html', About = about )