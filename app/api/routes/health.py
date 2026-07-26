# app/api/routes/health.py

from fastapi import APIRouter, status

from app.core.config import settings
from app.utils.datetime_utils import iso_datetime

router = APIRouter(tags=["Health"])


@router.get("/health", status_code=status.HTTP_200_OK)
async def health():
    return {
        "status": "ok",
        "timestamp": iso_datetime,
        "service": settings.app_name,
    }
