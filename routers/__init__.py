""" package_init"""
from fastapi import APIRouter
from routers import users, example, debug
import os

router = APIRouter()

router.include_router(users.router)
router.include_router(example.router)

# 本番では有効にならないようにBINDで設定
if os.getenv("BIND") == "127.0.0.1":
    router.include_router(debug.router)
