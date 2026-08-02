# app/models/response/error_response.py

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    status: int
    code: str
    message: str
