from flask import Blueprint

main = Blueprint('main', __name__, template_folder='../templates')


from app.main import routes
