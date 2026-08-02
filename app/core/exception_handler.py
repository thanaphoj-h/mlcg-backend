# app/core/exception_handler.py

from fastapi import FastAPI, Request
from fastapi import status as http_status
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.utils.response_utils import create_http_error_response


# HTTP_401_UNAUTHORIZED
# HTTP_404_NOT_FOUND
# HTTP_405_METHOD_NOT_ALLOWED
async def http_exception_handler(_request: Request, exception: StarletteHTTPException) -> JSONResponse:

    return create_http_error_response(
        status_code=exception.status_code, message=str(exception.detail), headers=exception.headers
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(http_status.HTTP_400_BAD_REQUEST, http_exception_handler)
    app.add_exception_handler(http_status.HTTP_401_UNAUTHORIZED, http_exception_handler)
    app.add_exception_handler(http_status.HTTP_404_NOT_FOUND, http_exception_handler)
    app.add_exception_handler(http_status.HTTP_405_METHOD_NOT_ALLOWED, http_exception_handler)
