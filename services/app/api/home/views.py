from flask import (
    Flask,
    Blueprint,
    render_template
)
from ..helpers.http_status_codes import HTTP_200_OK

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