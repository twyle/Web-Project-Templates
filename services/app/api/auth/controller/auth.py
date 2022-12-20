from flask import url_for, redirect
from ..models.user import User
from ...extensions.extensions import bcrypt, db


def handle_registration(form):
    """Handle user registration."""
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(
        username=form.username.data,
        email=form.email.data,
        password=hashed_password
    )
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('auth.login'))


def handle_login(form):
    """Handle user login."""
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        return redirect(url_for('home.home_page'))