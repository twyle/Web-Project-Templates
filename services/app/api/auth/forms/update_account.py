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
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), 
        Length(min=2, max=20)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    picture = FileField('Update Profile Picture', 
        validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose another.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose another.')