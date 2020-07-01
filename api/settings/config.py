import os
from broker.services.authentication.auth import (
    authenticate,
    authenticate_dev,
)
from broker.services.logging import log
from broker.settings.additional import TestJWT

basedir = os.path.abspath(os.path.dirname(__file__))
log.info(f"Base Directory: {basedir}")


class Config:
    """
    Common configuration class
    """
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False

    STATUS = "Red"

    TESTING: bool = False
    DEVELOPMENT: bool = False
    STAGING: bool = False
    PRODUCTION: bool = False

    SWAGGER: bool = True
    AUTHENTICATE = authenticate


class TestConfig(Config):
    """
    Test environment configurations, inherit Config as base class, possibly add another as
    sub class.
    """
    """
       Development environment configurations, inherit Config as base class.
       """
    ENV = "Testing"
    TESTING = True
    DEBUG = True
    STATUS = "Green"
    FIREBASE = False
    AUTHENTICATE = authenticate_dev

    # aws
    AWS_REGION: str = "eu-west-1"

    # logging details
    LOGGER: str = "sanic-python-api"
    LOG_DEBUG: bool = False

    # postgres sql
    DB_DRIVER = "asyncpg"
    DB_HOST = "0.0.0.0"
    DB_PORT = 5432
    DB_USER = "root"
    DB_PASSWORD = "root"
    DB_DATABASE = "postgres"

    # redis
    REDIS: dict = dict(
        address=("127.0.0.1", 6379),
        db=0,
        interface="",
        encoding="utf-8",
    )

    # API - for swagger
    URL_VERSION_PREFIX = "v1"
    API_VERSION = "1.0"
    API_TITLE = "Sanic Python Api"
    API_DESCRIPTION = "Sanic-Python basic api setup"
    API_PRODUCES_CONTENT_TYPES = ["application/json"]
    API_CONSUMES_CONTENT_TYPES = ["application/json"]
    API_CONTACT_EMAIL = "kevinsmith.kis@gmail.com"
    API_BASEPATH = "/"
    API_SCHEMES = ["http"]

    SWAGGER_UI_CONFIGURATION = {
        "validatorUrl": None,  # Disable Swagger validator
        "displayRequestDuration": True,
        "docExpansion": "none",
    }

    API_SECURITY = [{"authToken": []}]

    API_SECURITY_DEFINITIONS = {
        "authToken": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": 'Paste your auth token and do not forget to add "Bearer " in front of '
                           'it',
        }
    }

    # jwt - only for statging/dev/testing
    SANIC_JWT_SECRET: str = "3ea4891f385355ca00b143546819a13e0f9d5f24a2b044a70249d98b5cd2ff95"
    SANIC_JWT_ACCESS_TOKEN_NAME: str = "access_token"  # token?
    SANIC_JWT_ALGORITHM: str = "HS256"
    SANIC_JWT_EXPIRY = int(2 * 60 * 60)  # 3 hours
    SANIC_JWT_REFRESH_EXPIRY = int(14 * 24 * 60 * 60)

    JWT_TEST_CONFIG = TestJWT


class DevelopmentConfig(Config):
    """
    Development environment configurations, inherit Config as base class.
    """
    ENV = "Development"
    DEVELOPMENT = True
    DEBUG = True
    STATUS = "Green"

    # logging details
    LOGGER: str = "sanic-python-api"
    LOG_DEBUG: bool = False

    # redis
    REDIS: dict = dict(
        address=("127.0.0.1", 6379),
        db=0,
        interface="",
        encoding="utf-8",
    )

    # API - for swagger
    URL_VERSION_PREFIX = "v1"
    API_VERSION = "1.0"
    API_TITLE = "Sanic Python Api"
    API_DESCRIPTION = "Sanic-Python basic api setup"
    API_PRODUCES_CONTENT_TYPES = ["application/json"]
    API_CONSUMES_CONTENT_TYPES = ["application/json"]
    API_CONTACT_EMAIL = "kevinsmith.kis@gmail.com"
    API_BASEPATH = "/"
    API_SCHEMES = ["http"]

    SWAGGER_UI_CONFIGURATION = {
        "validatorUrl": None,  # Disable Swagger validator
        "displayRequestDuration": True,
        "docExpansion": "none",
    }

    API_SECURITY = [{"authToken": []}]

    API_SECURITY_DEFINITIONS = {
        "authToken": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": 'Paste your auth token and do not forget to add "Bearer " in front of '
                           'it',
        }
    }

    # jwt
    SANIC_JWT_SECRET: str = "3ea4891f385355ca00b143546819a13e0f9d5f24a2b044a70249d98b5cd2ff95"
    SANIC_JWT_ACCESS_TOKEN_NAME: str = "access_token"
    SANIC_JWT_ALGORITHM: str = "HS256"
    SANIC_JWT_EXPIRY = int(2 * 60 * 60)  # 3 hours
    SANIC_JWT_REFRESH_EXPIRY = int(14 * 24 * 60 * 60)


class StagingConfig(Config):
    """
    Staging environment configurations, inherit Config as base class.
    """
    ENV = "Staging"
    STAGING = True
    DEBUG = True
    STATUS = "Green"

    # aws
    AWS_REGION: str = "eu-west-1"

    # logging details
    LOGGER: str = "sanic-python-api"
    LOG_DEBUG: bool = False

    # redis
    REDIS: dict = dict(
        address=("127.0.0.1", 6379),  # dns name for redis service
        db=0,
        interface="",
        encoding="utf-8",
    )

    # API - for swagger
    URL_VERSION_PREFIX = "v1"
    API_VERSION = "1.0"
    API_TITLE = "Sanic Python Api"
    API_DESCRIPTION = "Sanic-Python basic api setup"
    API_PRODUCES_CONTENT_TYPES = ["application/json"]
    API_CONSUMES_CONTENT_TYPES = ["application/json"]
    API_CONTACT_EMAIL = "kevinsmith.kis@gmail.com"
    API_BASEPATH = "/"
    API_SCHEMES = ["http"]

    SWAGGER_UI_CONFIGURATION = {
        "validatorUrl": None,  # Disable Swagger validator
        "displayRequestDuration": True,
        "docExpansion": "none",
    }

    API_SECURITY = [{"authToken": []}]

    API_SECURITY_DEFINITIONS = {
        "authToken": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": 'Paste your auth token and do not forget to add "Bearer " in front of '
                           'it',
        }
    }

    # jwt
    SANIC_JWT_SECRET: str = "3ea4891f385355ca00b143546819a13e0f9d5f24a2b044a70249d98b5cd2ff95"
    SANIC_JWT_ACCESS_TOKEN_NAME: str = "access_token"
    SANIC_JWT_ALGORITHM: str = "HS256"
    SANIC_JWT_EXPIRY = int(2 * 60 * 60)  # 3 hours
    SANIC_JWT_REFRESH_EXPIRY = int(14 * 24 * 60 * 60)


class ProductionConfig(Config):
    """
    Production environment configurations, inherit Config as base class.
    """
    ENV = "Production"
    PRODUCTION = True
    DEBUG = False
    STATUS = "Green"
    SWAGGER = False

    # aws
    AWS_REGION: str = "eu-west-1"

    # logging details
    LOGGER: str = "sanic-python-api"
    LOG_DEBUG: bool = False

    # redis
    REDIS: dict = dict(
        address=("127.0.0.1", 6379),  # dns name for redis service
        db=0,
        interface="",
        encoding="utf-8",
    )

    # API - for swagger
    URL_VERSION_PREFIX = "v1"
    API_VERSION = "1.0"
    API_TITLE = "Sanic Python Api"
    API_DESCRIPTION = "Sanic-Python basic api setup"
    API_PRODUCES_CONTENT_TYPES = ["application/json"]
    API_CONSUMES_CONTENT_TYPES = ["application/json"]
    API_CONTACT_EMAIL = "kevinsmith.kis@gmail.com"
    API_BASEPATH = "/"
    API_SCHEMES = ["http"]

    SWAGGER_UI_CONFIGURATION = {
        "validatorUrl": None,  # Disable Swagger validator
        "displayRequestDuration": True,
        "docExpansion": "none",
    }

    API_SECURITY = [{"authToken": []}]

    API_SECURITY_DEFINITIONS = {
        "authToken": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": 'Paste your auth token and do not forget to add "Bearer " in front of '
                           'it',
        }
    }

    # jwt
    SANIC_JWT_SECRET: str = "3ea4891f385355ca00b143546819a13e0f9d5f24a2b044a70249d98b5cd2ff95"
    SANIC_JWT_ACCESS_TOKEN_NAME: str = "access_token"
    SANIC_JWT_ALGORITHM: str = "HS256"
    SANIC_JWT_EXPIRY = int(2 * 60 * 60)  # 3 hours
    SANIC_JWT_REFRESH_EXPIRY = int(14 * 24 * 60 * 60)


config_by_name = dict(
    TEST=TestConfig,
    DEV=DevelopmentConfig,
    STAGING=StagingConfig,
    PROD=ProductionConfig
)
