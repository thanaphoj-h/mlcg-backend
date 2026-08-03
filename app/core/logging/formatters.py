# app/core/logging/formatters.py

import logging

from app.constants.logging_constants import LOG_DATE_FORMAT, LOG_FORMAT


def create_log_formatter() -> logging.Formatter:
    return logging.Formatter(fmt=LOG_FORMAT, datefmt=LOG_DATE_FORMAT)
