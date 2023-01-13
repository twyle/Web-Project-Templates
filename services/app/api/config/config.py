import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    """Base configuration."""

    DEBUG = True 
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")
    PASSWORD_RESET_SALT = os.environ.get('PASSWORD_RESET_SALT', 'salt')
    
    POSTGRES_HOST = os.environ["POSTGRES_HOST"]
    POSTGRES_DB = os.environ["POSTGRES_DB"]
    POSTGRES_PORT = os.environ["POSTGRES_PORT"]
    POSTGRES_USER = os.environ["POSTGRES_USER"]
    POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]

    db_conn_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SQLALCHEMY_DATABASE_URI = db_conn_string
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_USERNAME = os.environ["MAIL_USERNAME"]
    MAIL_PASSWORD = os.environ["MAIL_PASSWORD"]
    MAIL_SERVER = os.environ["MAIL_SERVER"]
    MAIL_PORT = os.environ["MAIL_PORT"]
    MAIL_USE_SSL = os.environ["MAIL_USE_SSL"]
    MAIL_DEFAULT_SENDER = os.environ["MAIL_DEFAULT_SENDER"]


class DevelopmentConfig(BaseConfig):
    """Development confuguration."""
    DEBUG = True 
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")


class TestingConfig(BaseConfig):
    """Testing configuration."""

    TESTING = True
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")


class ProductionConfig(BaseConfig):
    """Production configuration."""

    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")


Config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "staging": ProductionConfig,
}
