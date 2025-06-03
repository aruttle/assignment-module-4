from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()  # Declare outside so it can be reused

def create_app():
    app = Flask(__name__)

    # Secret key for session management and CSRF protection
    app.config['SECRET_KEY'] = 'your-secret-key'

    # PostgreSQL connection URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Cottage087@localhost:5432/glamping'

    # Disable tracking modifications to save resources
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)  # This was correct — no need to redeclare migrate locally

    # Register blueprints
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

