from flask import (
    Flask,
    Blueprint,
    render_template,
    redirect,
    url_for
)
from .forms.register import RegistrationForm
from .forms.login import LoginForm
from .controller.auth import (
    handle_registration,
    handle_login
) 

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm() 
    if form.validate_on_submit():
        return handle_registration(form)
    return render_template('auth/register.html', title='Register', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return handle_login(form)
    return render_template('auth/login.html', title='Login', form=form)