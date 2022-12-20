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
from ..models.user import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), 
        Length(min=2, max=20)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=2, max=20)])
    confirm_password = PasswordField('Confirm Password', 
    validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose another.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose another.')