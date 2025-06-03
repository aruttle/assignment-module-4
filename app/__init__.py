from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Secret key for session management and CSRF protection
    app.config['SECRET_KEY'] = 'your-secret-key'

    # PostgreSQL connection URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Cottage087@localhost:5432/glamping'

    # Disable tracking modifications to save resources
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Register blueprints
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

