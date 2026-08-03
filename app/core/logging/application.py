# app/core/logging/application.py

import logging

from app.constants.logging_constants import LOG_ROTATE_SIZE_TYPE, LOG_ROTATE_TIME_TYPE
from app.core.config import settings
from app.core.logging.filters import RequestUUIDFilter
from app.core.logging.formatters import create_log_formatter
from app.core.logging.handlers import create_console_handler, create_rotating_file_handler, create_timed_file_handler


def setup_application_logging() -> None:

    log_rotate_type = settings.log_rotate_type.upper()
    formatter = create_log_formatter()
    request_uuid_filter = RequestUUIDFilter()

    # Console Handler
    console_handler = create_console_handler(formatter=formatter, request_uuid_filter=request_uuid_filter)

    # File Handler
    if log_rotate_type == LOG_ROTATE_SIZE_TYPE:
        file_handler = create_rotating_file_handler(
            log_file=settings.log_path,
            max_bytes=int(settings.log_rotate_max_size),
            backup_count=settings.log_rotate_backup_count,
            formatter=formatter,
            request_uuid_filter=request_uuid_filter,
        )
    elif log_rotate_type == LOG_ROTATE_TIME_TYPE:
        file_handler = create_timed_file_handler(
            log_file=settings.log_path,
            when=settings.log_rotate_when,
            interval=settings.log_rotate_interval,
            backup_count=settings.log_rotate_backup_count,
            formatter=formatter,
            request_uuid_filter=request_uuid_filter,
        )
    else:
        raise ValueError(rf"Unsupported log rotation type: {log_rotate_type!r}")

    root_logger = logging.getLogger()
    root_logger.setLevel(settings.log_level.upper())
    root_logger.handlers.clear()
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    logging.captureWarnings(True)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
