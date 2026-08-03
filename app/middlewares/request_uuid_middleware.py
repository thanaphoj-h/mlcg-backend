# app/middlewares/request_uuid_middleware.py

from uuid import UUID

from fastapi import Request, Response
from fastapi import status as http_status
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from app.constants.constants import API_V1_PATH, INVALID_REQUEST_UUID_MSG, MISSING_REQUEST_UUID_MSG, REQUEST_UUID_HEADER
from app.utils.response_utils import create_http_error_response
from app.core.logging.context import set_request_uuid, reset_request_uuid


class RequestUUIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        if not request.url.path.startswith(API_V1_PATH):
            return await call_next(request)

        request_uuid = request.headers.get(REQUEST_UUID_HEADER)

        if request_uuid is None:
            return create_http_error_response(
                status_code=http_status.HTTP_400_BAD_REQUEST, message=MISSING_REQUEST_UUID_MSG, headers=None
            )

        try:
            parsed_uuid = UUID(request_uuid)
            if parsed_uuid.version != 4:
                raise ValueError("Only UUID v4 is supported")

            normalized_uuid = str(parsed_uuid)

        except ValueError:
            return create_http_error_response(
                status_code=http_status.HTTP_400_BAD_REQUEST, message=INVALID_REQUEST_UUID_MSG, headers=None
            )

        # Store the request UUID for use during the current request.
        request.state.request_uuid = normalized_uuid

        # Set the request UUID context
        token = set_request_uuid(normalized_uuid)

        try:

            # Continue processing the request.
            response = await call_next(request)
            # Include the request UUID in the response headers.
            response.headers[REQUEST_UUID_HEADER] = normalized_uuid

            return response
        finally:
            # Restore the previous request UUID context
            reset_request_uuid(token)
