from flask_login import UserMixin
from app import db, login_manager

# Define User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # Add any additional fields or methods as needed

# Define user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
