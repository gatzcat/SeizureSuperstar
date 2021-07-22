
from datetime import datetime, date
from flask import Flask, flash, redirect, render_template, request, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from wtforms import BooleanField, DateField, SelectField, StringField, PasswordField, validators
from wtforms.fields.core import DateTimeField, IntegerField, SelectMultipleField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import InputRequired, EqualTo, Email, Length

from variables import *

# Initialising Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '\x05\x1bl\xd7\xfc\xfd\r\xf7N\xb5\x16\x8f\x1f)\x00\\jL*=\x16\r\xcc\xe4'

# Ensure templates are auto-reloaded
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Initialising Flask-Login
login_manager = LoginManager()
login_manager.init_app(app) 
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# Initialising SQLAlchemy and a whole lot of DB defining ahead
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finalproject.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Table for login credentials
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(37), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(280), nullable=False)


class Medison(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medication = db.Column(db.String(50), nullable=False)
    pills_number = db.Column(db.Integer, nullable=False)
    pills_mg = db.Column(db.Integer, nullable=False)
    daily_freq = db.Column(db.Integer, nullable=False)
    duedate = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Chronolog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    seizure_type = db.Column(db.String(50), db.ForeignKey('tldr.seizure_type'))
    duration = db.Column(db.Integer, nullable=False)
    pre_ictal = db.Column(db.String(500))
    during = db.Column(db.String(500))
    post_ictal = db.Column(db.String(500))
    triggers = db.Column(db.String(500), db.ForeignKey('tldr.triggers'))
    emergency_meds = db.Column(db.String(50))
    ambulance = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Tldr(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)   
    startdate = db.Column(db.Date, nullable=False)
    diagnosis = db.Column(db.String(500))
    diagnosis_description = db.Column(db.String(500))
    family_history = db.Column(db.String(50))
    fh_description = db.Column(db.String(500))
    pre_ictal = db.Column(db.String(30))
    pre_symptoms = db.Column(db.String(500))
    pre_extra = db.Column(db.String(800))
    seizure_description = db.Column(db.String(800))
    seizure_extra = db.Column(db.String(800))
    post_ictal = db.Column(db.String(50))
    post_symptoms = db.Column(db.String(500))
    post_extra = db.Column(db.String(500))
    triggers = db.Column(db.String(50))
    triggers_description = db.Column(db.String(500))
    triggers_extra = db.Column(db.String(500))
    current_meds = db.Column(db.String(50))
    cmeds_name = db.Column(db.String(500))
    prev_meds = db.Column(db.String(50))
    pmeds_name = db.Column(db.String(500))
    diet = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Drwhen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, nullable=False)
    doc_name = db.Column(db.String(50), nullable=False)
    hosp_name = db.Column(db.String(100), nullable=False)
    appointment_type = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Login form


class Login(FlaskForm):
    username = StringField('username', validators=[InputRequired('Missing Username'),
                           Length(min=4, max=37, message='Must be between 4 and 37 characters')])
    password = PasswordField('password', validators=[InputRequired(
        'Missing Password'), Length(min=6, message='Must be at least 6 characters')])
    remember = BooleanField('remember me')

# Registration form


class Register(FlaskForm):
    username = StringField('username', validators=[InputRequired('Missing Username'),
                           Length(min=4, max=37, message='Must be between 4 and 37 characters')])
    email = StringField('email', validators=[InputRequired('Missing Email'), Email('Invalid Email')])
    password = PasswordField('password', validators=[InputRequired('Missing Password'), EqualTo(
        'confirm', message='Passwords must match!'), Length(min=6, message='Must be at least 6 characters')])
    confirm = PasswordField('Repeat Password', validators=[InputRequired('Please reconfirm your password')])


# TLDRepeat form
class Tldr(FlaskForm):
    name = StringField('Name', validators=[InputRequired('Please provide this information')])
    age = StringField('Age', validators=[InputRequired('Please provide this information')])
    startdate = DateField('Seizure Start Date', validators=[InputRequired('Please provide this information')])
    diagnosis = SelectField('Diagnosis', choices=[('have a'), ('don\'t have a')], validators=[InputRequired('Please provide this information')])
    diagnosis_description = TextAreaField('Diagnosis Details (if any)')
    family_history = SelectField('Diagnosis', choices=[('have a'), ('don\'t have any'), ('am not sure about')], validators=[InputRequired('Please provide this information')])
    fh_description = TextAreaField('Family History Details (if any)')
    pre_ictal = SelectField('Any Pre-seizure Symptoms?', choices=[('always can'), ('occasionally can'), ('cannot')], validators=[InputRequired('Please provide this information')])
    pre_symptoms = SelectMultipleField('Pre-ictal symptoms? (if any)', choices=PRE_ICTAL)
    pre_extra = TextAreaField('Any other descriptions or symptoms')
    seizure_description = SelectMultipleField('Seizure Description', choices=DURING)
    seizure_extra = _extra = TextAreaField('Any other descriptions or symptoms')
    post_ictal = StringField('Post-ictal symptoms?', validators=[InputRequired('Please provide this information')])
    post_symptoms = SelectMultipleField('Post-ictal symptoms?', choices=POST_ICTAL)
    post_extra = TextAreaField('Any other descriptions or symptoms')
    triggers = SelectField('Trigger Description', choices=[('know'), ('do not know')], validators=[InputRequired('Please provide this information')])
    trigger_description = SelectMultipleField('Trigger Description', choices=TRIGGERS)
    trigger_extra = TextAreaField('Other Triggers')
    current_meds = SelectField('Current Medication', choices=[('am'), ('am not')])
    cmeds_name = SelectMultipleField('Current Medication', choices=MEDICATION)
    prev_meds = SelectField('Previous Medication', choices=[('have'), ('have not')])
    pmeds_name = SelectMultipleField('Previous Medication', choices=MEDICATION)
    diet = SelectField('Diet Type', choices=[('Regular'), ('Vegetarian'), ('Vegan'), ('Ketogenic'), ('Paleo'), ('Gluten-free'), ('Dairy-free'), ('Pescetarians'), ('Paleo')], validators=[InputRequired('Please provide this information')])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Register()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            password = generate_password_hash(form.password.data, method='sha256')

            # Add new user data to the db
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()

            flash('You have been registered successfully. Please login!')
            return redirect('/login')

        # If form does not validate, or if page accessed by GET, user sent back to index 
        return render_template('index.html', form=form)
    else:
        return render_template('index.html', form=form)


@app.route('/tldrepeat')
@login_required
def tldrepeat():
    form = Tldr()
    return render_template('tldr.html', form=form)


@app.route('/drwhen')
@login_required
def drwhen():
    return render_template('drwhen.html')


@app.route('/chronolog')
@login_required
def loggy():
    return render_template('chronolog.html')


@app.route('/medison')
@login_required
def medison():
    return render_template('medison.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = form.username.data
            password = form.password.data
            
            # Check user table for said user profile
            profile = User.query.filter_by(username=user).first()

            if profile and check_password_hash(profile.password, password):
                login_user(profile, remember=form.remember.data)
                flash(user + ', you\'re logged in successfully. Woohoo!')
                return redirect('/')
            flash('Invalid Username or Password')
                    
        # If form does not validate, or if page accessed by GET, user sent back to login 
        return render_template('login.html', form=form)
    else:
        return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully. Come back soon!')
    return redirect('/')
