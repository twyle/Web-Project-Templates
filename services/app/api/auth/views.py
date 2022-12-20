from flask import (
    Flask,
    Blueprint,
    render_template
)
from .forms.register import RegistrationForm
from .forms.login import LoginForm

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('auth/register.html', title='Register', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('auth/login.html', title='Login', form=form)