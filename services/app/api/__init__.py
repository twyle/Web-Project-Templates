from flask import Flask
from .helpers.error_handlers import register_error_handlers
from .helpers.helpers import (
    set_configuration,
    check_configuration,
    register_blueprints,
    register_extensions
)
from .helpers.http_status_codes import HTTP_200_OK
from .extensions.extensions import db
import sys
from .logging.logger import app_logger


def create_app():
    """"Create the Flask App instance."""

    app = Flask(__name__)
    set_configuration(app)
    app_logger.info("Set the configurations!")

    try:
        check_configuration()
    except Exception as e:
        app_logger.critical(str(e))
        sys.exit(1)

    register_extensions(app)
    app_logger.info("Registered the extensions!")
    register_error_handlers(app)
    app_logger.info("Registered the error handlers!")
    register_blueprints(app)
    app_logger.info("Registered the blueprints!")

    @app.route("/health")
    def health_check():
        """Check if the application is running."""
        return jsonify({"success": "hello from flask"}), HTTP_200_OK

    app.shell_context_processor({"app": app, "db": db})

    return app