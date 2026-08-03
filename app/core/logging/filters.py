# app/core/logging/filters.py

import logging

from app.core.logging.context import get_request_uuid


class RequestUUIDFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.request_uuid = get_request_uuid()
        return True
