# SEIZURE SUPERSTAR
#### Video Demo:  https://www.youtube.com/watch?v=EZsmZ-JI3xU
#### Description:

**Last Updated: 27AUG**

## Introduction
**Seizure Superstar** is a web app designed to help people who suffer from seizures. 

My partner has refractory epilepsy, and this inspired me to design my CS50 Final Project. Whilst we have used several handy mobile apps, they only exists as a mobile app and it is not possible to access your data through a web browser. Unfortunately, we have not been able to find a similar app that is web-based.

The initial idea was to make the web app applicable for different chronic conditions. However this was scaled down to just epilepsy in order to be thorough. With additional information about other chronic conditions, the webapp could potentially be reconfigured to help those who suffer from other conditions.
_________
## Made with
- Python (3.8.10)
- HTML5
- Bootstrap 5
- Flask
    - Flask-login
    - Wtforms & Flask-Wtf
    - SQLAlchemy & Flask-SQLAlchemy
- SQLite3
_________
## Features
- [x] Working user creation and user login 
- [x] TLDRepeat:
    - A cloze passage style form for the user to provide their condition and seizure details. 
    - The aim of the form is to consolidate all the most relevant information about the user's condition so that they will not have to keep "repeating the same old story" each and every time they see a new health professional.
    - The data collected from the form can be used to feed the options of the other pages  
    - This will be the first step for the newly registered user.
- [x] Medison:
    - Simple Calculator that will calculate from the number of remaining pills and daily dosage and display the date a pharmacy run must be done to replenish medication
    - The list of medication fed to this page comes from the TLDR info collected
- [x] Dr When+:
    - A complete log of the user's appointments both past and future. This will allow the user to scroll through their appointments and see their evolution
- [x] Chronolog
    - This is a log of the user's seizures that will hopefully allow them to observe patterns 
_________
## Files
### `README.md` file
This file was part of the requisite of the Final Project, which perhaps some human may read at some point of time.
### `requirements.txt` file
A standard requirements.txt file, with a list of the modules required and used for this project

### `static` folder
#### Lightning.ico
Graphic used for the login page
#### style.css
self-explanatory

### `templates` folder


#### formhelpers.html 
A helper file with macros for Flask-wtform which simplifies the creation of the form fields. Spoiler: There is a huge amount of forms in this project

### `app.py` file
Where all the python code and quite a number of tears reside

### `variables.py` file
The main app.py file was getting really long and tedious to go through so some functions and arrays were placed here to save one from scrolling through alllll the nitty-gritty

### `finalproject.db`
Sqlite3 database used for the tables

### meds.csv
A list of all the current branded medication used for seizures and epilepsy. It was way too long to make into an array manually. I left it as a separate .csv file so that if it has to be updated as (hopefully) more drugs and treatments become developed, one will not have to go through any codes.
_________
## Wishlist of Improvements
* Neater and more elegant code
* Fix known bugs
* Addional languages supported
* Fancy charts from the SQL data
* Sorting the seizure log via values with JS
* Better front-end management interface when I hopefully gain some JS proficiency
* Allow user to download their logs or send to email
* Integration with calendar app for notifications and/or reminders for pharmacy runs and appointments.
* Possibility of scaling up to other chronic illnesses
_________
## Acknowledgements
I'm very grateful for:
- The staff of CS50, for the amazing course, lectures, and material. 
- My partner, who believes in me more than I do and always encourages me. She also has to put up with my sulking and whining throughout this course and daily life.
- Helpful coursemates and seniors in the Discord Channel
- Select friends and acquaintances, who also egg me on
