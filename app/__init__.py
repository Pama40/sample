from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Create Flask application instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.db'


# Initialize SQLAlchemy
db = SQLAlchemy(app)
app.app_context().push()

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Import your views and models here
from app import views, models

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
