from flask_login import UserMixin
from app import db, login_manager
from flask_sqlalchemy import SQLAlchemy

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

db = SQLAlchemy()

class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=True)
    postal_code = db.Column(db.String(10), nullable=True)
    last_updated = db.Column(db.DateTime, nullable=True)
