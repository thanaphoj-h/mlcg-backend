# app/main.py

from fastapi import FastAPI

from app.api.router import api_router
from app.middlewares.api_key_middleware import APIKeyMiddleWare
from app.middlewares.request_uuid_middleware import RequestUUIDMiddleware

app = FastAPI()

app.add_middleware(APIKeyMiddleWare)
app.add_middleware(RequestUUIDMiddleware)
app.include_router(api_router)
