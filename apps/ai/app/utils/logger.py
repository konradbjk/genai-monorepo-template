import os
import logging
import sys
from .settings import settings

LOG_LEVEL = settings.log_level.name

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(levelname)-8s - %(name)s - %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "stream": sys.stdout
        }
    },
    "loggers": {
        "buyermind": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
            "propagate": False
        }
    }
}

logging.config.dictConfig(logging_config)


def setup_logger(name: str) -> logging.Logger:
    """
    Creates and caches a logger instance.

    Args:
        name: Name of the module/pipeline (e.g., 'api', 'generate_bm_version')

    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(f"monorepo.{name}")
    logger.setLevel(LOG_LEVEL)
    return logger
