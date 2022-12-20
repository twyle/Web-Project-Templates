from flask import Flask
from .helpers.error_handlers import register_error_handlers
from .helpers.helpers import (
    register_blueprints
)
from .helpers.http_status_codes import HTTP_200_OK


def create_app():
    """"Create the Flask App instance."""

    app = Flask(__name__)

    register_error_handlers(app)
    register_blueprints(app)

    @app.route("/health")
    def health_check():
        """Check if the application is running."""
        return jsonify({"success": "hello from flask"}), HTTP_200_OK

    app.shell_context_processor({"app": app})

    return app