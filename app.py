
from datetime import datetime, date
from flask import Flask, flash, redirect, render_template, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.orm import backref
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from wtforms import BooleanField, DateField, SelectField, StringField, PasswordField
from wtforms.fields.core import DateTimeField, IntegerField, SelectMultipleField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import InputRequired, EqualTo, Email, Length, Optional

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
    seizure_type = db.Column(db.String(50), nullable=False)
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
    age = db.Column(db.String(50), nullable=False)   
    startdate = db.Column(db.String(50), nullable=False)
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
    trigger_description = db.Column(db.String(500))
    trigger_extra = db.Column(db.String(500))
    current_meds = db.Column(db.String(50))
    cmeds_name = db.Column(db.String(500))
    prev_meds = db.Column(db.String(50))
    pmeds_name = db.Column(db.String(500))
    diet = db.Column(db.String(50))
    datetime = db.Column(db.DateTime, default=datetime.utcnow)
    tldr = db.relationship('User', backref='TLDR')
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
required = validators = [InputRequired('Please provide this information')]

option = validators = [Optional()]


class Tldrepeat(FlaskForm):
    name = StringField('Name', required)
    age = StringField('Age', required)
    startdate = StringField('Seizure Start Date', required)
    diagnosis = SelectField('Diagnosis', required, choices=[('have a'), ('don\'t have a')])
    family_history = SelectField('Diagnosis', required, choices=[('have a'), ('don\'t have any'), ('am not sure about')])
    pre_ictal = SelectField('Any Pre-seizure Symptoms?', required, choices=[('always can'), ('occasionally can'), ('cannot')])
    seizure_description = SelectMultipleField('Seizure Description', required, choices=DURING)
    post_ictal = StringField('Post-ictal symptoms?', required)
    triggers = SelectField('Trigger Description', required, choices=[('know'), ('do not know')])
    current_meds = SelectField('Current Medication', required, choices=[('am'), ('am not')])
    prev_meds = SelectField('Previous Medication', required, choices=[('have'), ('have not')])
    diet = SelectField('Diet Type', required, choices=[('Regular'), ('Vegetarian'), ('Vegan'),
                                                       ('Ketogenic'), ('Paleo'), ('Gluten-free'), ('Dairy-free'), ('Pescetarians'), ('Paleo')])
    diagnosis_description = TextAreaField('Diagnosis Details (if any)', option)
    fh_description = TextAreaField('Family History Details (if any)', option)
    pre_symptoms = SelectMultipleField('Pre-ictal symptoms? (if any)', option, choices=PRE_ICTAL)
    pre_extra = TextAreaField('Any other descriptions or symptoms', option)
    seizure_extra = TextAreaField('Any other descriptions or symptoms', option)
    post_symptoms = SelectMultipleField('Post-ictal symptoms?', option, choices=POST_ICTAL)
    post_extra = TextAreaField('Any other descriptions or symptoms', option)
    trigger_description = SelectMultipleField('Trigger Description', option, choices=TRIGGERS)
    trigger_extra = TextAreaField('Other Triggers', option)
    cmeds_name = SelectMultipleField('Current Medication', option, choices=MEDICATION)
    pmeds_name = SelectMultipleField('Previous Medication', option, choices=MEDICATION)
    

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
            logout_user()

            flash('You have been registered successfully. Please login!')
            return redirect('/login')

        # If form does not validate, or if page accessed by GET, user sent back to index 
        return render_template('index.html', form=form)
    else:
        return render_template('index.html', form=form)


@app.route('/tldrepeat', methods=['GET', 'POST'])
@login_required
def tldrepeat():
    exist = Tldr.query.filter_by(user_id=current_user.id).order_by(Tldr.id.desc()).first()
    form = Tldrepeat()
    if request.method == 'POST':
        if form.validate_on_submit():

            pre_symptoms = unlist(form.pre_symptoms.data, PRE_ICTAL)
            print(pre_symptoms)
            
            post_symptoms = unlist(form.post_symptoms.data, POST_ICTAL)
            print(post_symptoms)

            cmeds_name = unlist(form.cmeds_name.data, MEDICATION)
            print(cmeds_name)
            
            trigger_description = unlist(form.trigger_description.data, TRIGGERS)
            print(trigger_description)
            
            pmeds_name = unlist(form.pmeds_name.data, MEDICATION)
            print(pmeds_name)
            
            seizure_description = unlist(form.seizure_description.data, DURING)
            print(seizure_description)


            tldr = Tldr(name=form.name.data, age=form.age.data, startdate=form.startdate.data, diagnosis=form.diagnosis.data, diagnosis_description=form.diagnosis_description.data, 
                        family_history=form.family_history.data, fh_description=form.fh_description.data, pre_ictal=form.pre_ictal.data, pre_extra=form.pre_extra.data, seizure_extra=form.seizure_extra.data, 
                        post_ictal=form.post_ictal.data, post_extra=form.post_extra.data, triggers=form.triggers.data, 
                        trigger_extra=form.trigger_extra.data, current_meds=form.current_meds.data, 
                        prev_meds=form.prev_meds.data, diet=form.diet.data, user_id=current_user.id, pre_symptoms=pre_symptoms, post_symptoms=post_symptoms, cmeds_name=cmeds_name, trigger_description=trigger_description, pmeds_name=pmeds_name, seizure_description=seizure_description)
            db.session.add(tldr)
            db.session.commit()
            print(Tldr.query.filter_by(user_id=current_user.id).all())

            flash('Great Job!')
            return redirect('tldrepeat')
        else:
            flash('Something went wrong')
            return render_template('tldr.html', form=form, exist=exist)
    else:
        return render_template('tldr.html', form=form, exist=exist)


@app.route('/drwhen')
@login_required
def drwhen():
    return render_template('drwhen.html')


@app.route('/chronolog')
@login_required
def chronolog():
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
