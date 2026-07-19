# app/api/routes/health.py

from datetime import UTC, datetime

from fastapi import APIRouter, status

from app.core.config import settings

router = APIRouter(tags=["Health"])


@router.get("/health", status_code=status.HTTP_200_OK)
async def health():
    return {
        "status": "ok",
        "timestamp": datetime.now(UTC).isoformat(),
        "service": settings.app_name,
    }
