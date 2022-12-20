from ..home.views import home
from ..auth.views import auth
import os
from ..config.config import Config
from ..extensions.extensions import (
    db,
    ma,
    bcrypt,
    login_manager,
    cors,
    migrate
)


def set_configuration(app):
    config_name = os.environ.get('FLASK_ENV', 'development')
    app.config.from_object(Config[config_name])


def register_blueprints(app):
    app.register_blueprint(home)
    app.register_blueprint(auth, url_prefix='/auth')


def register_extensions(app):
    """Register the app extensions."""
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    # login_manager.login_message_category = 'info'