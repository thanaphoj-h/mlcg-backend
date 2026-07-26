# app/utils/datetime_utils.py

from datetime import datetime
from zoneinfo import ZoneInfo

from app.core.config import settings

def local_now() -> datetime:
    return datetime.now(ZoneInfo(settings.timezone))

def iso_datetime() -> str:
    return local_now().isoformat()
