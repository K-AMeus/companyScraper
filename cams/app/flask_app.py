from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from . import db
from .routes import api_bp

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pass@localhost/cams'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the app
    db.init_app(app)

    # for interaction with frontend
    CORS(app)

    from .routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
