from sanic import response
from sanic.views import HTTPMethodView
from sanic_openapi import doc
from sanic_jwt.decorators import protected

from api.services.logging import log
from api.services.redis.ping.ping import online as redis_online


class Health(HTTPMethodView):
    """
    Health check endpoint, this service is intended to check operational status of the api api.
    """

    @doc.tag("Health")
    @doc.summary("Health check on api api.")
    async def get(self, request):
        """
        API health check, GET method.
        :param request: framework based application object.
        :return: response json: (dict): health object
        """
        # app config
        config = request.app.config

        # redis
        try:
            r_online = await redis_online(request.app.redis)
            log.info(f"Redis Online: {redis_online}")

        except Exception as e:
            log.error(f"Redis Health check exception: {e}")
            r_online = False

        # api available
        # TODO: insert a check here a integration API.

        # redis session details if available.
        if r_online:
            redis_session = request["session"]

            if not redis_session.get("health_count"):
                redis_session["health_count"] = 0

            redis_session["health_count"] += 1
            log.info(f"Health check counter: {redis_session['health_count']}")

        return response.json(
            status=200,
            body={
                "Health": config.get("STATUS"),
                "Version": config.get("API_VERSION"),
                "Environment": config.get("ENV"),
                "Redis": r_online,
                "Counter": request["session"]["health_count"],
                "Connection API status": "TODO",
            }
        )


class HealthProtected(HTTPMethodView):
    """
    Health check endpoint, this service is intended to check operational status of the api api.
    """

    @doc.tag("Health")
    @doc.summary("Health check on api api with authentication protection")
    @doc.exclude(True)
    @protected()
    async def get(self, request):
        """
        API health check, GET method.
        :param request: framework based application object.
        :return: response json: (dict): health object
        """
        # app config
        config = request.app.config

        # redis
        try:
            r_online = await redis_online(request.app.redis)
            log.info(f"Redis Online: {redis_online}")

        except Exception as e:
            log.error(f"Redis Health check exception: {e}")
            r_online = False

        # api available
        # TODO: insert a check here a integration API.

        # redis session details if available.
        if r_online:
            redis_session = request["session"]

            if not redis_session.get("health_count"):
                redis_session["health_count"] = 0

            redis_session["health_count"] += 1
            log.info(f"Health check counter: {redis_session['health_count']}")

        return response.json(
            status=200,
            body={
                "Health": config.get("STATUS"),
                "Version": config.get("API_VERSION"),
                "Environment": config.get("ENV"),
                "Redis": r_online,
                "Counter": request["session"]["health_count"],
                "Connection API status": "TODO",
            }
        )
