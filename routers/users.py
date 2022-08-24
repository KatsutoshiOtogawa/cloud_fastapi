""" This is a program"""

from enum import Enum
from typing import Any, Optional
from fastapi import APIRouter, Body
from pydantic import BaseModel, Field

# userのrouter
router = APIRouter()

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
    price: float = Field(
        gt=0
    )
    tax: Optional[float] = None

class User(BaseModel):
    username: str 
    full_name: Optional[str] = None

@router.get("/")
async def root() -> dict[str, str]:
    """
        aaa
    """
    return {"message": "Hello World"}

@router.get("/items/{item_id}")
def read_item(item_id: int, aaa: Optional[str] = None):
    """
        例です。商品ではこのルートは消してください。
    """
    return {"item_id": item_id, "q": aaa}

@router.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "aaaa"}
    return {"model_name": model_name, "message": "bbb"}

@router.get("/query/")
async def read_item2(skip: int=0, limit: int=3):
    return {"skip": skip, "limit": limit}

@router.get("/query2/{item_id}")
async def read_item3(item_id: str,abc: int, qqq: Optional[str] = None):
    return {"item_id": item_id, "abc": abc, "qqq": qqq}

@router.post("/post/")
async def create_item(item: Item):
    item.description + item.name
    return item

@router.put("/items/aaa/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: int = Body(gt=0),
    qa: Optional[str] = None

):
    results = {
        "item_id": item_id,
        "item": item,
        "user": user,
        "importance": importance
    }

    if qa:
        results.update({"qa": qa})
    return results

@router.put("/items/bbb/{item_id}")
async def update_item2(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results


@router.put("/items/ccc/{item_id}")
async def update_item3(
    item_id: int,
    item: Item = Body(
        example={
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        }
    )
) -> dict[str, Any]:
    results = {
        "item_id": item_id,
        "item": item,
    }
    return results

@router.put("/items/ddd/{item_id}")
async def update_item4(
    item_id: int,
    item: Item = Body(
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "price": 35.4,
                    "tax": 3.2,
                }
            },
            "converted": {
                "summary": "An example with coverted data",
                "description": "Fast API can convert price `strings` to actual `numbers` automatical",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                }
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                }
            }
        }
    )
):
    results = {"item_id": item_id, "item": item}
    return results


