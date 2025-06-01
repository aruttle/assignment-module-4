from flask import render_template
from app.main import main
from app.models import Project

@main.route('/')
def home():
    projects = Project.query.all()
    return render_template('home.html', projects=projects)
@main.route('/about')
def about():
    return render_template('about.html')
@main.route('/accommodations')
def accommodations():
    projects = Project.query.all()
    return render_template('accommodations.html', projects=projects)

