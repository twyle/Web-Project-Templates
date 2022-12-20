from flask import Flask, request
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
from .helpers.hooks import (
    get_exception, 
    get_response, 
    log_get_request, 
    log_post_request
) 


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

    # @app.before_first_request
    # def application_startup():
    #     """Log the beginning of the application."""
    #     app_logger.info("Web app is up!")

    # @app.before_request
    # def log_request():
    #     """Log the data held in the request."""
    #     if request.method in {"POST", "PUT"}:
    #         log_post_request()
    #     elif request.method in {"GET", "DELETE"}:
    #         log_get_request()

    # @app.after_request
    # def log_response(response):
    #     """Log the data held in the response."""
    #     try:
    #         get_response(response)
    #     except Exception:
    #         pass
    #     finally:
    #         return response

    # @app.teardown_request
    # def log_exception(exc):
    #     """Log the data held in the exception."""
    #     get_exception(exc)

    @app.route("/health")
    def health_check():
        """Check if the application is running."""
        return jsonify({"success": "hello from flask"}), HTTP_200_OK

    app.shell_context_processor({"app": app, "db": db})

    return app