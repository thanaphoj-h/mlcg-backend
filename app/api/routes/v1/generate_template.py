# app/api/routes/v1/generate_template.py

from fastapi import APIRouter
from fastapi import status as http_status

from app.models.response.standard_response import StandardResponse
from app.utils.response_utils import create_success_response
from app.core.logging.application import get_logger

logger = get_logger(__name__)

router = APIRouter(tags=["PDF TEMPLATE"])


@router.post("/generate_template", response_model=StandardResponse, status_code=http_status.HTTP_200_OK)
async def generate_template():
    logger.info("Called Generate Template (v1)")
    return create_success_response(data={"message": "Template generated successfully"})
