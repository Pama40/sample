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
    if current_user.is_authenticated:  # Check if the user is already authenticated
        return redirect(url_for('welcome'))  # Redirect them to the welcome page

    form = LoginForm()  # Instantiate the login form

    if form.validate_on_submit():  # Check if the form is submitted and valid
        user = User.query.filter_by(username=form.username.data).first()  # Query the user from the database
        if user and user.check_password(form.password.data):  # Check if the user exists and the password is correct
            login_user(user)  # Log in the user
            next_page = request.args.get('next')  # Get the next page from the URL query parameters
            return redirect(
                next_page or url_for('welcome'))  # Redirect to the next page if provided, else to the welcome page

    return render_template('login.html', form=form)  # Render the login form


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
        user.password_hash=form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/welcome')
#@login_required
def welcome():
    return render_template('welcome.html')
@app.route('/diet')
def diet():
    return render_template('dietary_control.html')
@app.route('/ingredient')
def ingredient():
    return render_template('ingredient.html')
@app.route('/generate_recipe', methods=['GET', 'POST'])
#@login_required
def generate_recipe():
    # Your code to handle generating recipes from ingredients
    return render_template('generate_recipe.html')
@app.route('/option',methods=['GET','POST'])
def option():
    return render_template('option.html')
@app.route('/profile')
#@login_required add this
def profile():
    # Logic to fetch and display user profile information
    return render_template('profile.html')

@app.route('/choose_option')
@login_required
def choose_option():
    # This page allows users to choose between diet and recipe options
    return render_template('choose_option.html')

# You can add more routes as needed for additional functionalities
