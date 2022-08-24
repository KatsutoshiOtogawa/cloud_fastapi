"""This is a test program."""
import os
from fastapi import FastAPI

from routers import router

openAPIDisable = { "docs_url": None, "redoc_url": None, "openapi_url": None }

app:FastAPI
# K_SERVICEがセットされているかどうかでCloudRun無いかそうでないかをチェック。
if os.getenv("K_SERVICE") is None:
    app = FastAPI()
else:
    app = FastAPI(**openAPIDisable)

app.include_router(router)
