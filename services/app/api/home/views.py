from flask import (
    Flask,
    Blueprint,
    render_template,
    url_for,
    redirect,
    request,
    current_app
)
from ..helpers.http_status_codes import HTTP_200_OK
from flask_login import current_user, login_required
from ..auth.forms.update_account import UpdateAccountForm
from ..extensions.extensions import db
import secrets
import os 
from PIL import Image


home = Blueprint('home', __name__)

@home.route('/')
@home.route('/home')
@home.route('/index')
def home_page():
    return render_template('home/index.html', title='home'), HTTP_200_OK


@home.route('/about')
def about_page():
    return render_template('home/about.html', title='about'), HTTP_200_OK

@home.route('/contact')
def contact_page():
    return render_template('home/contact.html', title='contact'), HTTP_200_OK


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/img', picture_fn)
    
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    return picture_fn


@home.route('/account', methods=['GET', 'POST'])
@login_required
def account_page():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_fn = save_picture(form.picture.data)
            current_user.image_file = picture_fn
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('home.account_page'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template('home/account.html', 
        title='account', 
        image_file=image_file, form=form
        ), HTTP_200_OK