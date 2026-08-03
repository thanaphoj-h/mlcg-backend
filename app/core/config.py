# app/core/config.py

from typing import Literal

from pydantic import ByteSize, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "BACKEND"

    api_port: int = 8000
    api_host: str = "0.0.0.0"
    api_key: str

    timezone: str = "UTC"

    debug: bool = False

    access_log_enable: bool = True
    log_level: str = "INFO"
    log_path: str = "logs/app.log"

    log_rotate_type: Literal["time", "size"] = "time"
    log_rotate_when: str = "midnight"
    log_rotate_interval: int = 1
    log_rotate_max_size: ByteSize = Field(default="10MiB", validate_default=True)
    log_rotate_backup_count: int = 10

    model_config = SettingsConfigDict(env_file=(".env", ".env.local"), env_file_encoding="utf-8")


settings = Settings()
