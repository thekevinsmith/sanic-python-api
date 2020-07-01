import logging
import sys

from enum import IntEnum
import aiotask_context as context


class LogLevel(IntEnum):
    DEBUG: int = 10
    INFO: int = 20
    WARN: int = 30


DEFAULT_LOG_LEVEL = LogLevel.INFO


class RequestIdFilter(logging.Filter):
    def filter(self, record):
        record.request_id = context.get("Request-Id", "")
        record.request_id = context.get("X-Request-ID", "")
        return True


LOGGING_CONF = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"requestid": {"()": RequestIdFilter}},
    "formatters": {
        "simple": {
            "format": (
                "%(asctime)s - (%(name)s)[%(levelname)s] %(process)d/%(threadName)s/"
                "%(funcName)s:%(lineno)d : %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "access": {
            "format": (
                "%(asctime)s - (%(name)s)[%(levelname)s][%(host)s] : "
                "%(request)s %(message)s %(status)d %(byte)d"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "api": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": sys.stdout,
        },
        "errorFile": {
            "class": "logging.FileHandler",
            "formatter": "simple",
            "filename": "api/logs/api_stderr.log",
        },
        "brokerFile": {
            "class": "logging.FileHandler",
            "formatter": "simple",
            "filename": "api/logs/api.log",
        },
    },
    "loggers": {
        "api-log": {
            "level": DEFAULT_LOG_LEVEL,
            "levels": [10, 20, 30],
            "handlers": ["api", "brokerFile"],
        },
        "sanic": {
            "level": DEFAULT_LOG_LEVEL,
            "handlers": [
                "api",
                "errorStream",
                "errorFile",
            ],
        },
    },
}
