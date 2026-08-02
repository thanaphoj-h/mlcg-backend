# app/api/router.py

from fastapi import APIRouter

from app.api.routes.health import router as health_router
from app.api.routes.v1.generate_template import router as generate_template_router
from app.constants.constants import API_PREFIX, API_V1_PREFIX

api_router = APIRouter(prefix=API_PREFIX)
api_v1_router = APIRouter(prefix=API_V1_PREFIX)

api_router.include_router(health_router)

api_router.include_router(api_v1_router)  # Add /v1 Router
api_v1_router.include_router(generate_template_router)
