# __init__.py
from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config
from datetime import timedelta

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Session configuration
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SECURE'] = True  # Set to True for production
    app.config['SESSION_COOKIE_SAMESITE'] = 'None'  # Allow cross-site cookies

    # Initialize extensions
    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    # Configure CORS - Add your frontend domain
    CORS(app, 
         origins=["https://chyrp-aniket.up.railway.app", "http://localhost:3000"], 
         supports_credentials=True,
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
         allow_headers=["Content-Type", "Authorization"])
    
    # Import and register blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    return app

# Add this to your __init__.py after creating the app
@app.after_request
def after_request(response):
    # Allow credentials
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    
    # Allow specific headers
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    
    # Allow specific methods
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    
    return response
