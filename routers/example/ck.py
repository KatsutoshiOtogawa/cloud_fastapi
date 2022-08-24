""" This is a program"""

from typing import Any, Optional
from uuid import UUID
from datetime import datetime, time, timedelta
from fastapi import APIRouter,Cookie, Path, Body
from pydantic import BaseModel, Field

# userのrouter
router = APIRouter()

@router.get("/ck/", tags=["cookie_example"])
async def read_items(abs_id: Optional[str] = Cookie(default=None)):
    """
    """
    return {"abs_id", abs_id}
