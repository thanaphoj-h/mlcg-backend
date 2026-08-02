# app/utils/response_utils.py

from collections.abc import Mapping
from http import HTTPStatus
from typing import Any

from fastapi import status as http_status
from starlette.responses import JSONResponse

from app.models.response.error_response import ErrorResponse
from app.models.response.metadata_response import MetadataResponse
from app.models.response.standard_response import StandardResponse
from app.utils.datetime_utils import iso_datetime


def create_health_response():
    return {"status": "ok", "timestamp": iso_datetime()}


def create_success_response(*, data: Any = None, status_code: int = http_status.HTTP_200_OK) -> StandardResponse:
    return StandardResponse(data=data, error=None, metadata=MetadataResponse(status=status_code))


def create_error_response(*, status_code: int, code: str, message: str) -> StandardResponse:
    return StandardResponse(
        data=None,
        error=[ErrorResponse(status=status_code, code=code, message=message)],
        metadata=MetadataResponse(status=status_code),
    )


def create_http_error_response(
    *, status_code: int, message: str | None = None, headers: Mapping[str, str] | None = None
) -> JSONResponse:

    status_info = HTTPStatus(status_code).name
    message = message or HTTPStatus(status_code).phrase

    response = create_error_response(status_code=status_code, code=status_info, message=message)

    headers = dict(headers) if headers else None
    return JSONResponse(status_code=status_code, content=response.model_dump(mode="json"), headers=headers)
