"""This is a test program."""
import os
from fastapi import FastAPI # pylint: disable=import-error

from routers import users

openAPIDisable = { "docs_url": None, "redoc_url": None, "openapi_url": None }

app:FastAPI
# K_SERVICEがセットされているかどうかでCloudRun無いかそうでないかをチェック。
if os.getenv("K_SERVICE") is None:
    app = FastAPI()
else:
    app = FastAPI(**openAPIDisable)

app.include_router(users.router)
