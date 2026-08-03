# app/constants/logging_constants.py

from typing import Final

LOG_FORMAT: Final[str] = (
    "%(asctime)s.%(msecs)03d | %(levelname)-8s | %(name)s | request_uuid=%(request_uuid)s | %(message)s"
)
LOG_DATE_FORMAT: Final[str] = "%Y-%m-%d %H:%M:%S"
LOG_FILE_DATE_SUFFIX_FORMAT: Final[str] = "%Y%m%d"
LOG_FILE_DATE_SUFFIX_PATTERN: Final[str] = r"^\d{8}$"
LOG_ROTATE_TIME_TYPE: Final[str] = "TIME"
LOG_ROTATE_SIZE_TYPE: Final[str] = "SIZE"

DEFAULT_REQUEST_UUID: Final[str] = "-"

HTTP_EXCEPTION_LOG_FORMAT: Final[str] = "HTTP exception | method=%s, path=%s, status_code=%s, detail=%s"
