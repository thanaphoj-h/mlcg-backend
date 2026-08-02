# app/core/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "BACKEND"

    api_port: int = 8000
    api_host: str = "0.0.0.0"
    api_key: str

    timezone: str = "UTC"

    debug: bool = False

    log_level: str = "INFO"

    model_config = SettingsConfigDict(env_file=(".env", ".env.local"), env_file_encoding="utf-8")


settings = Settings()
