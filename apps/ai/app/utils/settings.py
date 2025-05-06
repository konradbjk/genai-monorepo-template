from pydantic_settings import BaseSettings, SettingsConfigDict
from enum import Enum


class EnvEnum(str, Enum):
    development = "development"
    production = "production"


class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class Settings(BaseSettings):
    env: EnvEnum = EnvEnum.development
    log_level: LogLevel = LogLevel.INFO
    port: int = 8080
    openai_api_key: str
    mongodb_uri: str
    qdrant_url: str = 'http://localhost:6333/'
    nvidia_api_key: str
    mongodb_database_name: str = "documents"
    langchain_tracking_v2: bool = True
    langchain_api_key: str
    langchain_project: str = 'development'

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
