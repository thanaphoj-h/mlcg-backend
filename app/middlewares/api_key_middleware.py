# app/middleware/api_key_middleware.py

from secrets import compare_digest

from fastapi import Request, Response
from fastapi import status as http_status
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from app.constants.constants import API_KEY_HEADER, API_V1_PATH, INVALID_API_KEY_MSG
from app.core.config import settings
from app.utils.response_utils import create_http_error_response


class APIKeyMiddleWare(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:

        if not request.url.path.startswith(API_V1_PATH):
            return await call_next(request)

        api_key = request.headers.get(API_KEY_HEADER)

        if api_key is None or not compare_digest(api_key, settings.api_key):
            return create_http_error_response(
                status_code=http_status.HTTP_401_UNAUTHORIZED, message=INVALID_API_KEY_MSG, headers=None
            )

        return await call_next(request)
