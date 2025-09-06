# config.py
import os
from datetime import timedelta
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    
    # Railway provides DATABASE_URL environment variable
    if os.environ.get('DATABASE_URL'):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')
    else:
        # Fallback to MySQL
        DB_HOST = os.environ.get('DB_HOST') or 'localhost'
        DB_PORT = os.environ.get('DB_PORT') or '3306'
        DB_NAME = os.environ.get('DB_NAME') or 'blog_db'
        DB_USER = os.environ.get('DB_USER') or 'blog_user'
        DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'blog_password'
        SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
