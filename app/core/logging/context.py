# app/core/logging/context.py

from contextvars import ContextVar, Token

from app.constants.logging_constants import DEFAULT_REQUEST_UUID

_request_uuid: ContextVar[str] = ContextVar("request_uuid", default=DEFAULT_REQUEST_UUID)


def get_request_uuid() -> str:
    return _request_uuid.get()


def set_request_uuid(request_uuid: str) -> Token[str]:
    return _request_uuid.set(request_uuid)


def reset_request_uuid(token: Token[str]) -> None:
    _request_uuid.reset(token)
