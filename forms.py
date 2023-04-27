from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import PasswordField, BooleanField

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class UploadForm(FlaskForm):
    submit = SubmitField('Upload')

class SourceForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired(), URL()])
    name = StringField('Name', validators=[DataRequired()])
    city = StringField('City')
    postal_code = StringField('Postal Code')
    submit = SubmitField('Submit')

class AdminLoginForm(FlaskForm):
    master_password = PasswordField('Master Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    is_admin = BooleanField('Is Admin')
    submit = SubmitField('Submit')
