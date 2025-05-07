"""MongoDB Utilities"""
import re

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import OperationFailure

from .settings import settings, EnvEnum
from .logger import setup_logger

APP_ENV = settings.env.name

logger = setup_logger("mongodb-client")


def mask_connection_string(conn_str: str) -> str:
    """
    Mask the username and password in a MongoDB connection string.

    For example:
      Input: "mongodb://user:secret@localhost:27017/mydb"
      Output: "mongodb://***:***@localhost:27017/mydb"
    """
    # This regex pattern matches the URL prefix, capturing the username and password.
    pattern = r"(mongodb:\/\/)([^:]+):([^@]+)@"
    return re.sub(pattern, r"\1***:***@", conn_str)


if APP_ENV == EnvEnum.production:
    logger.info("Connecting to production MongoDB %s",
                mask_connection_string(settings.mongodb_uri))
    mongo_client = MongoClient(
        settings.mongodb_uri,
        tls=True,
        retryWrites=False,
        maxPoolSize=50,
        minPoolSize=10,
        maxIdleTimeMS=60000,
        waitQueueTimeoutMS=2000,
        serverSelectionTimeoutMS=5000,
        connectTimeoutMS=5000
    )
else:
    logger.info("Connecting to local MongoDB %s", settings.mongodb_uri)
    mongo_client = MongoClient(
        settings.mongodb_uri,
        authSource="admin",
        maxPoolSize=50,
        minPoolSize=10,
        maxIdleTimeMS=60000,
        waitQueueTimeoutMS=2000,
        serverSelectionTimeoutMS=5000,
        connectTimeoutMS=5000,
        tls=False
    )
