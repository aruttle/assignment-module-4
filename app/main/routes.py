# from flask import render_template
# from app.main import main
# from app.models import Guest, Accommodation, Booking 


# @main.route('/')
# def home():
#     projects = Project.query.all()
#     return render_template('home.html', projects=projects)
# @main.route('/about')
# def about():
#     return render_template('about.html')
# @main.route('/accommodations')
# def accommodations():
#     projects = Project.query.all()
#     return render_template('accommodations.html', projects=projects)
from flask import render_template
from app.main import main
from app.models import Accommodation


@main.route('/')
def home():
    return render_template('home.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/accommodations')
def accommodations():
    accommodations = Accommodation.query.all()
    return render_template('accommodations.html', accommodations=accommodations)


