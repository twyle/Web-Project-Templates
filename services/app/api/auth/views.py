from flask import (
    Flask,
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash
)
from .forms.register import RegistrationForm
from .forms.login import LoginForm
from .forms.request_reset import RequestPasswordResetForm
from .forms.reset_password import ResetPasswordForm
from .controller.auth import (
    handle_registration,
    handle_login
) 
from flask_login import logout_user, current_user
from .models.user import User
from ..extensions.extensions import mail, bcrypt, db
from flask_mail import Message


auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home.home_page'))
    form = RegistrationForm() 
    if form.validate_on_submit():
        return handle_registration(form)
    return render_template('auth/register.html', title='Register', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.home_page'))
    form = LoginForm()
    if form.validate_on_submit():
        return handle_login(form)
    return render_template('auth/login.html', title='Login', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.home_page'))

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', 
        sender='lyceokoth@gmail.com',
        recipients=[user.email])
    link = url_for('auth.reset_password', token=token, _external=True)
    msg.body = f"Click on the following link to reset your password {link}"
    mail.send(msg)
    

@auth.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home.home_page'))
    form = RequestPasswordResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions on how to rewset your password!')
        return redirect(url_for('home.home_page'))
    return render_template('auth/reset_request.html', title='Reset Password', form=form)


@auth.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('home.home_page'))
    user = User.verify_reset_token(token)
    if not user:
        print(f'That is an invalid or expired token! {token}')
        flash('That is an invalid or expired token!')
        return redirect(url_for('auth.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated. You are now able to log in!')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_token.html', title='Reset Password', form=form)