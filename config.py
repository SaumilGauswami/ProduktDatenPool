import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'your_secret_key'
SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/database_name'
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
ALLOWED_EXTENSIONS = {'csv'}

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
