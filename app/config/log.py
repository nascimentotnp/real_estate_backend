import logging
from logging import config

import asgi_correlation_id

json_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "request_id_filter": {
            "()": "config.log.RequestIdLogFilter"
        }
    },
    "formatters": {
        "json_correlation": {
            "format": "%(asctime)s %(levelname)s [%(correlation_id)s] %(threadName)s %(filename)s %(funcName)s %(lineno)s %(message)s",
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter"
        }
    },
    "handlers": {
        "json_correlation": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "json_correlation",
            "stream": "ext://sys.stdout",
            "filters": ["request_id_filter"]
        }
    },
    "loggers": {
        "root": {
            "level": "INFO",
            "handlers": ["json_correlation"]
        }
    }
}


class RequestIdLogFilter(logging.Filter):
    def filter(self, record):
        record.correlation_id = asgi_correlation_id.correlation_id.get()
        return True


def setup_log():
    logging.config.dictConfig(json_config)

