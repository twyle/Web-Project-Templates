from ..home.views import home


def register_blueprints(app):
    app.register_blueprint(home)