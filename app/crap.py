# @app.route('/', methods=['GET', 'POST'])
# @app.route('/index', methods=['GET', 'POST'])
# def index():
#     form = IndexForm()
    
#     if form.login.validate_on_submit() and form.login.submit.data:
#         user = query_db('SELECT * FROM Users WHERE username="{}";'.format(form.login.username.data), one=True)
#         if user == None:
#             flash('Sorry, this user does not exist!')
#         elif user['password'] == form.login.password.data:
#             return redirect(url_for('stream', username=form.login.username.data))
#         else:
#             flash('Sorry, wrong password!')
#     elif form.register.validate_on_submit() and form.register.submit.data:
#         query_db('INSERT INTO Users (username, first_name, last_name, password) VALUES("{}", "{}", "{}", "{}");'.format(form.register.username.data, form.register.first_name.data,
#         form.register.last_name.data, form.register.password.data))
#         return redirect(url_for('index'))
#     return render_template('index.html', title='Welcome', form=form)


# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[InputRequired(message="Username required"), Length(min=8, max=25, message="Outside limitations")], render_kw={'placeholder': 'Username'})
#     password = PasswordField('Password', validators=[InputRequired(message="Password required"), Length(min=8, max=25, message="Outside limitations")], render_kw={'placeholder': 'Password'})
#     remember_me = BooleanField('Remember me') # TODO: It would be nice to have this feature implemented, probably by using cookies
#     submit = SubmitField('Sign In')

# class RegisterForm(FlaskForm):
#     first_name = StringField('First Name', validators=[InputRequired(message="First name required"), Length(min=2, max=25, message="First name must contain between 2 and 25 characters")], render_kw={'placeholder': 'First Name'})
#     last_name = StringField('Last Name', validators=[InputRequired(message="Last name required"), Length(min=2, max=25, message="Last name must contain between 2 and 25 characters")], render_kw={'placeholder': 'Last Name'})
#     username = StringField('Username', validators=[InputRequired(message="Username required"), Length(min=8, max=25, message="Username must contain between 8 and 25 characters")], render_kw={'placeholder': 'Username'})
#     password = PasswordField('Password', validators=[InputRequired(message="Password required"), Length(min=8, max=25, message="Password must contain between 2 and 25 characters")], render_kw={'placeholder': 'Password'})
#     confirm_password = PasswordField('Confirm Password', validators=[InputRequired(message="Password required"), EqualTo('password', message="Password must match")], render_kw={'placeholder': 'Confirm Password'})
#     submit = SubmitField('Sign Up')
                    


#                     from flask import render_template, flash, redirect, url_for, request
# from app import app, query_db
# from app.forms import PostForm, FriendsForm, ProfileForm, CommentsForm, RegisterForm, LoginForm, IndexForm
# from datetime import datetime
# from passlib.hash import pbkdf2_sha256 #pip install passlib

# import os

# # this file contains all the different routes, and the logic for communicating with the database

# # home page/login/registration
# @app.route('/', methods=['GET', 'POST'])
# @app.route('/index', methods=['GET', 'POST'])
# def index():
#     form = IndexForm()

#     flash(form.errors)
#     if form.login.validate_on_submit():
#         username_entered = form.login.username.data
#         password_entered = form.login.password.data

#         user = query_db('SELECT * FROM Users WHERE username="{}";'.format(username_entered), one=True)
#         if user == None:
#             flash("Username or password incorrect")
#         elif not pbkdf2_sha256.verify(password_entered, user['password']):
#             flash("Username or password incorrect")
#         elif pbkdf2_sha256.verify(password_entered, user['password']):
#             return redirect(url_for('stream', username=username_entered))
#     elif form.register.validate_on_submit():
#         username = form.register.username.data
#         password = form.register.password.data
        
#         encrypt_pswd = pbkdf2_sha256.hash(password) #Hashes and adds a 16byte salt, by default adds 29000 iterations. 
#         user = query_db('SELECT * FROM Users WHERE username="{}";'.format(username), one=True)
#         if user == None:
#             query_db('INSERT INTO Users (username, first_name, last_name, password) VALUES("{}", "{}", "{}", "{}");'.format(form.register.username.data, form.register.first_name.data,
#             form.register.last_name.data, encrypt_pswd))
#             return redirect(url_for('index')), flash('New user registered!')
#         else:
#             flash('Username already exists.')
#     return render_template('index.html', title='Welcome', form=form)
