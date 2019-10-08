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
                    