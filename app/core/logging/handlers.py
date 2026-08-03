# app/core/logging/handlers.py

import logging
import re
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from pathlib import Path

from app.constants.constants import UTF_8_ENCODING
from app.constants.logging_constants import LOG_FILE_DATE_SUFFIX_FORMAT, LOG_FILE_DATE_SUFFIX_PATTERN
from app.core.logging.filters import RequestUUIDFilter


def create_console_handler(
    *, formatter: logging.Formatter, request_uuid_filter: RequestUUIDFilter
) -> logging.StreamHandler:
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    handler.addFilter(request_uuid_filter)
    return handler


def create_timed_file_handler(
    *,
    log_file: str,
    when: str,
    interval: int,
    backup_count: int,
    formatter: logging.Formatter,
    request_uuid_filter: RequestUUIDFilter,
) -> TimedRotatingFileHandler:

    log_path = _create_log_path(log_file)

    handler = TimedRotatingFileHandler(
        filename=log_path,
        when=when,
        interval=interval,
        backupCount=backup_count,
        encoding=UTF_8_ENCODING,
        delay=True,
        utc=False,
    )

    handler.suffix = LOG_FILE_DATE_SUFFIX_FORMAT  # Set the date suffix format for rotated log files
    handler.setFormatter(formatter)  # Set the output formatter for each log record
    handler.addFilter(request_uuid_filter)  # Added the request UUID to each log record
    handler.extMatch = re.compile(LOG_FILE_DATE_SUFFIX_PATTERN, re.ASCII)  # Match rotated log file by date suffix

    return handler


def create_rotating_file_handler(
    *,
    log_file: str,
    max_bytes: int,
    backup_count: int,
    formatter: logging.Formatter,
    request_uuid_filter: RequestUUIDFilter,
) -> RotatingFileHandler:

    log_path = _create_log_path(log_file)

    handler = RotatingFileHandler(
        filename=log_path, maxBytes=max_bytes, backupCount=backup_count, encoding=UTF_8_ENCODING, delay=True
    )
    handler.setFormatter(formatter)  # Set the output formatter for each log record
    handler.addFilter(request_uuid_filter)  # Added the request UUID to each log record

    return handler


def _create_log_path(log_file: str) -> Path:
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    return log_path
