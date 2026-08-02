# app/api/routes/health.py

from fastapi import APIRouter
from fastapi import status as http_status

from app.utils.response_utils import create_health_response

router = APIRouter(tags=["Health"])


@router.get("/health", status_code=http_status.HTTP_200_OK)
async def health():
    return create_health_response()
