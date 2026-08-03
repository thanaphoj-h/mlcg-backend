# app/api/routes/health.py

from fastapi import APIRouter
from fastapi import status as http_status

from app.core.logging.application import get_logger
from app.utils.response_utils import create_health_response

logger = get_logger(__name__)


router = APIRouter(tags=["Health"])


@router.get("/health", status_code=http_status.HTTP_200_OK)
async def health():
    logger.info("Called Health Endpoint")
    return create_health_response()
