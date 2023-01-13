from flask_wtf import FlaskForm
from wtforms import (
    PasswordField,
    SubmitField
)
from wtforms.validators import (
    Length, 
    EqualTo, 
    InputRequired
)


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[InputRequired(), Length(min=2, max=20)])
    confirm_password = PasswordField('Confirm Password', 
    validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')