from flask import render_template
from app.main import main
from app.models import Project

@main.route('/')
def home():
    projects = Project.query.all()
    return render_template('home.html', projects=projects)
