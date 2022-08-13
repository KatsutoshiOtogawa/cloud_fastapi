"""This is a test program."""
import os
from enum import Enum
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

# routingに使ったらダメ。
# あくまで値選択でなおかつバレていいやつのみ。
class ModelName(str, Enum):
    """
        aaa
    """
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    description: Optional[str] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float
    tax: Optional[float] = None

openAPIDisable = { "docs_url": None, "redoc_url": None, "openapi_url": None }

app:FastAPI
# K_SERVICEがセットされているかどうかでCloudRun無いかそうでないかをチェック。
if os.getenv("K_SERVICE") is None:
    app = FastAPI()
else:
    app = FastAPI(**openAPIDisable)

@app.get("/")
async def root() -> dict[str, str]:
    """
        aaa
    """
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, aaa: Optional[str] = None):
    """
        例です。商品ではこのルートは消してください。
    """
    return {"item_id": item_id, "q": aaa}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "aaaa"}
    return {"model_name": model_name, "message": "bbb"}

@app.get("/query/")
async def read_item2(skip: int=0, limit: int=3):
    return {"skip": skip, "limit": limit}

@app.get("/query2/{item_id}")
async def read_item3(item_id: str,abc: int, qqq: Optional[str] = None):
    return {"item_id": item_id, "abc": abc, "qqq": qqq}

@app.post("/post/")
async def create_item(item: Item):
    item.description + item.name
    return item
