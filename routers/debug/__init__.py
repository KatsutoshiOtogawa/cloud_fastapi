""" package_init"""
from fastapi import APIRouter
from routers.debug import aaa

router = APIRouter()

router.include_router(aaa.router)
