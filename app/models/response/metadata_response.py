# app/models/response/metadata_response.py

from datetime import datetime

from fastapi import status as http_status
from pydantic import BaseModel, Field

from app.utils.datetime_utils import local_now


class MetadataResponse(BaseModel):
    status: int = http_status.HTTP_200_OK
    timestamp: datetime = Field(default_factory=local_now)
