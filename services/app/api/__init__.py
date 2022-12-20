from flask import Flask
from .helpers.error_handlers import register_error_handlers
from .helpers.helpers import (
    set_configuration,
    register_blueprints
)
from .helpers.http_status_codes import HTTP_200_OK
from .extensions.extensions import db


def create_app():
    """"Create the Flask App instance."""

    app = Flask(__name__)

    set_configuration(app)
    register_error_handlers(app)
    register_blueprints(app)

    @app.route("/health")
    def health_check():
        """Check if the application is running."""
        return jsonify({"success": "hello from flask"}), HTTP_200_OK

    app.shell_context_processor({"app": app, "db": db})

    return app