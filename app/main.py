# app/main.py

from fastapi import FastAPI

from app.api.router import api_router
from app.core.exception_handler import register_exception_handlers
from app.core.logging.application import setup_application_logging
from app.middlewares.api_key_middleware import APIKeyMiddleware
from app.middlewares.request_uuid_middleware import RequestUUIDMiddleware

setup_application_logging()

app = FastAPI()

register_exception_handlers(app)

# The last middleware added is processed first
app.add_middleware(RequestUUIDMiddleware)
app.add_middleware(APIKeyMiddleware)

app.include_router(api_router)
