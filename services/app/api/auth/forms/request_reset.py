from flask_wtf import FlaskForm
from wtforms import (
    StringField, SubmitField
)
from wtforms.validators import (
    ValidationError, 
    Email, 
    InputRequired
)
from ..models.user import User


class RequestPasswordResetForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('There is no account with that email. Please register first.')

