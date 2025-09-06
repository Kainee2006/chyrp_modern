from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    # Configure CORS
    CORS(app, supports_credentials=True)
    
    # Import and register blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    return app
