# app/models/response/metadata_response.py

from pydantic import BaseModel, Field
from datetime import datetime

from app.utils.datetime_utils import local_now

class MetadataResponse(BaseModel):
    status: int
    timestamp: datetime = Field(default_factory=local_now)

