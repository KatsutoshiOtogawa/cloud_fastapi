""" package_init"""
from fastapi import APIRouter
from routers.example import et

router = APIRouter()

router.include_router(et.router)
