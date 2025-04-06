# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)  # Allow frontend requests

    db.init_app(app)

    # Register Blueprints (later for auth, tasks etc.)
    from routes.task_routes import task_bp
    from routes.auth_routes import auth_bp

    app.register_blueprint(task_bp, url_prefix="/api/tasks")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    return app
