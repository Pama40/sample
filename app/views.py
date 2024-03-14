from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.models import User
from app.forms import LoginForm, RegistrationForm

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('welcome'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')  # Get the next page from the URL query parameters
            return redirect(next_page or url_for('welcome'))  # Redirect to the next page if provided, else to the welcome page
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('welcome'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@app.route('/generate_recipe', methods=['GET', 'POST'])
@login_required
def generate_recipe():
    # Your code to handle generating recipes from ingredients
    return render_template('generate_recipe.html')

@app.route('/profile')
@login_required
def profile():
    # Logic to fetch and display user profile information
    return render_template('profile.html')

@app.route('/choose_option')
@login_required
def choose_option():
    # This page allows users to choose between diet and recipe options
    return render_template('choose_option.html')

# You can add more routes as needed for additional functionalities
