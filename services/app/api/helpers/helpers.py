from ..home.views import home
from ..auth.views import auth
import os
from ..config.config import Config


def set_configuration(app):
    config_name = os.environ.get('FLASK_ENV', 'development')
    app.config.from_object(Config[config_name])


def register_blueprints(app):
    app.register_blueprint(home)
    app.register_blueprint(auth, url_prefix='/auth')