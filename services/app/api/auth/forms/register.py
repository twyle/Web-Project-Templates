from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, SubmitField
) 
from wtforms.validators import (
    ValidationError,
    DataRequired, 
    Length, 
    Email, 
    EqualTo, 
    InputRequired
)

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), 
        Length(min=2, max=20)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=2, max=20)])
    confirm_password = PasswordField('Confirm Password', 
    validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')