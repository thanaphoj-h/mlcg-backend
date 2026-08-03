# app/constants/constants.py

from typing import Final

# Common Constant
UTF_8_ENCODING = "utf-8"

# Middleware Constant
API_KEY_HEADER: Final[str] = "x-api-key"
INVALID_API_KEY_MSG: Final[str] = "Invalid or missing x-api-key header"
REQUEST_UUID_HEADER: Final[str] = "x-request-uuid"
MISSING_REQUEST_UUID_MSG: Final[str] = "Missing x-request-uuid header"
INVALID_REQUEST_UUID_MSG: Final[str] = "Invalid x-request-uuid header format; expected a valid UUID v4"

# API Router Constant
API_PREFIX: Final[str] = "/api"
API_V1_PREFIX: Final[str] = "/v1"
API_V1_PATH: Final[str] = f"{API_PREFIX}{API_V1_PREFIX}"
