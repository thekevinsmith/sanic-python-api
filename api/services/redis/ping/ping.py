from api.services.logging import log


async def online(redis):
    """
    Method to essentially ping the redis instance created in the config.
    :return: (bool): Indicates redis online
    """

    # Simple check to see if connection to firebase is online
    log.info(f"Redis call - {online}")

    redis_online = await redis.ping()

    print(redis_online)

    if redis_online == "PONG":
        return True

    else:
        return False
