from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FormField, TextAreaField, FileField, Form, validators, ValidationError
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, Length, EqualTo
# defines all forms in the application, these will be instantiated by the template,
# and the routes.py will read the values of the fields
# TODO: Add validation, maybe use wtforms.validators??
# TODO: There was some important security feature that wtforms provides, but I don't remember what; implement it



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(message="Username required"), Length(min=4, max=25, message="Outside limitations")], render_kw={'placeholder': 'Username'})
    password = PasswordField('Password', validators=[InputRequired(message="Password required"), Length(min=8, max=25, message="Outside limitations")], render_kw={'placeholder': 'Password'})

    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(message="First name required"), Length(min=2, max=25, message="First name must contain between 2 and 25 characters")], render_kw={'placeholder': 'First Name'})
    last_name = StringField('Last Name', validators=[InputRequired(message="Last name required"), Length(min=2, max=25, message="Last name must contain between 2 and 25 characters")], render_kw={'placeholder': 'Last Name'})
    username = StringField('Username', validators=[InputRequired(message="Username required"), Length(min=4, max=25, message="Username must contain between 4 and 25 characters")], render_kw={'placeholder': 'Username'})
    password = PasswordField('Password', validators=[InputRequired(message="Password required"), Length(min=8, max=25, message="Password must contain between 8 and 25 characters")], render_kw={'placeholder': 'Password'})
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(message="Password required"), EqualTo('password', message="Password must match")], render_kw={'placeholder': 'Confirm Password'})
    recaptcha = RecaptchaField()
    submit = SubmitField('Sign Up')


class IndexForm(FlaskForm):
    login = FormField(LoginForm)
    register = FormField(RegisterForm)

class PostForm(FlaskForm):
    content = TextAreaField('New Post', render_kw={'placeholder': 'What are you thinking about?'})
    image = FileField('Image')
    submit = SubmitField('Post')

class CommentsForm(FlaskForm):
    comment = TextAreaField('New Comment', render_kw={'placeholder': 'What do you have to say?'})
    submit = SubmitField('Comment')

class FriendsForm(FlaskForm):
    username = StringField('Friend\'s username', render_kw={'placeholder': 'Username'})
    submit = SubmitField('Add Friend')

class ProfileForm(FlaskForm):
    education = StringField('Education', render_kw={'placeholder': 'Highest education'})
    employment = StringField('Employment', render_kw={'placeholder': 'Current employment'})
    music = StringField('Favorite song', render_kw={'placeholder': 'Favorite song'})
    movie = StringField('Favorite movie', render_kw={'placeholder': 'Favorite movie'})
    nationality = StringField('Nationality', render_kw={'placeholder': 'Your nationality'})
    birthday = DateField('Birthday')
    submit = SubmitField('Update Profile')
