import aioredis
from sanic import Sanic
from sanic_cors import CORS
from sanic_jwt import initialize
from sanic_openapi import swagger_blueprint, doc
from sanic_session import Session, AIORedisSessionInterface, InMemorySessionInterface

from .endpoints import (
    health_blueprint,
    freshdesk_blueprint,
)
from .services.authentication.auth import (
    store_refresh_token,
    retrieve_refresh_token,
    retrieve_user,
)
from broker.services.aws.secrets_manager import AwsSecretsManager
from .settings.config import config_by_name
from .services.logging import log, LOGGING_CONF
from .services.firebase import Firebase

session = Session()

session_dispatch = {
    # "Testing": InMemorySessionInterface,
    "Testing": AIORedisSessionInterface,
    "Development": AIORedisSessionInterface,
    "Staging": AIORedisSessionInterface,
    "Production": AIORedisSessionInterface,
}


def create_app(name, config_name):
    """
    Application factory pattern for creating the Sanic object. Create the app as a Sanic class and
        initialize simple-bcrypt as the password hashing function.

    :param name: (string): the name of the application, configurable from manage.py
    :param config_name: (string): environment name TEST/DEV/STAGING/PROD

    :return: (class): Sanic application object.
    """
    # init sanic framework
    app = Sanic(name)

    # init configuration environment
    app.config.from_object(config_by_name[config_name])
    log.info(f"Environment loaded: {config_name}")

    # cors setup, disables all cookies, security, can lock in specific origin.
    CORS(
        app,
        resources={
            r"/swagger/*": {"origins": "*"},
            r"/v1/health/*": {"origins": "*"},
            r"/v1/authentication/*": {"origins": "*"},
        },
        automatic_options=True,
        supports_credentials=True,
    )

    # swagger blueprints, configuration
    swagger_blueprint.strict_slashes = True

    # init blueprints
    if app.config.SWAGGER:
        app.blueprint(swagger_blueprint)

    app.blueprint(health_blueprint)

    log.info(f"Load Blueprints:")
    for blueprint in app.blueprints:
        log.info(f"{blueprint}")

    # middleware security measure on response.
    @app.middleware("response")
    async def print_on_response(request, response):
        response.headers["x-xss-protection"] = "1; mode=block"
        response.headers["X-Content-Type-Options"] = "nosniff"

    @app.listener("before_server_start")
    async def before_broker_start(app, loop):
        try:
            log.info("Redis Setup")

            app.redis = await aioredis.create_redis_pool(
                address=app.config.REDIS.get("address"),
                encoding=app.config.REDIS.get("encoding"),
            )

            session.init_app(
                app=app,
                interface=session_dispatch[app.config.ENV](
                    redis=app.redis,
                    expiry=app.config.SANIC_JWT_EXPIRY,
                )
            )

            log.info("Redis Ping")
            await app.redis.ping()

        except Exception as e:
            log.error(f"Redis Connection Failed. {e}")

    #  initialize application authentication, configuration included in app config
    if not app.config.TESTING:
        initialize(
            app,
            authenticate=app.config.AUTHENTICATE,
            url_prefix=f"/v1/authentication",
            store_refresh_token=store_refresh_token,
            retrieve_refresh_token=retrieve_refresh_token,
            retrieve_user=retrieve_user,
            log_config=LOGGING_CONF,
        )
    else:
        initialize(
            app,
            authenticate=app.config.AUTHENTICATE,
            url_prefix=f"/v1/authentication",
            store_refresh_token=store_refresh_token,
            retrieve_refresh_token=retrieve_refresh_token,
            retrieve_user=retrieve_user,
            configuration_class=app.config.JWT_TEST_CONFIG,
        )

    try:
        secret_manager = AwsSecretsManager()
        secret = secret_manager.get_secret(app.config.AWS_FRESHDESK_SECRET_KEY)
        app.config.FRESDESK_AUTH = (secret.get("api_key"), secret.get("password"))
        log.info(f"FD Auth: {app.config.FRESDESK_AUTH}")

    except Exception as e:
        log.error(f"AWS Secret Manager Connection Failed. {e}")

    return app
