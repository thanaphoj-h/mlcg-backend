# app/models/response/standard_response.py

from typing import Any

from pydantic import BaseModel, Field

from app.models.response.error_response import ErrorResponse
from app.models.response.metadata_response import MetadataResponse


class StandardResponse(BaseModel):
    data: Any | None = None
    error: list[ErrorResponse] | None = None
    metadata: MetadataResponse = Field(default_factory=MetadataResponse)
