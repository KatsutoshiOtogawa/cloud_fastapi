""" This is a program"""

from enum import Enum
from typing import Any, Optional
from uuid import UUID
from datetime import datetime, time, timedelta
from fastapi import APIRouter, Body # pylint: disable=import-error
from pydantic import BaseModel, Field # pylint: disable=import-error

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

class ExampleTime(BaseModel):
    start_datetime: datetime = Field(
        title="In requests will be represented as a str in ISO 8601 format,like: 2022-08-14T17:20:53+09:00"
    )
    end_datetime: datetime = Field(
        title="In requests will be represented as a str in ISO 8601 format, like: 2022-08-14T17:20:53+09:00"
    )
    repeat_at: Optional[time] = Field(
        default=None, title="In requests and responses will be represented as a str in ISO 8601 format, like: 14:23:55.003"
    )
    process_after: Optional[timedelta] = Field(
        default=None, title="P4DT4H0M0.000000S,The description of the item"
    )

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



# 
@router.put("/items/eee/{item_id}", tags=["time_example"])
async def read_items(
    item_id: UUID,
    example_time: ExampleTime = Body(
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** Example time works correctly.",
                "value": {
                    "start_datetime": "2022-08-14T17:20:53+09:00",
                    "end_datetime": "2022-08-14T17:20:53+09:00",
                    "repeat_at": "14:23:55.003",
                    "process_after": "P1DT1H0M2.000000S",
                }
            },
            "converted": {
                "summary": "An example with coverted data",
                "description": "Fast API can convert price `strings` to actual `numbers` automatical",
                "value": {
                    "start_datetime": "2022-08-14T17:20:53+09:00",
                    "end_datetime": "2022-08-14T17:20:53+09:00",
                    "repeat_at": "14:23:55.003",
                    "process_after": "P1DT1H0M2.000000S",
                }
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "start_datetime": "2022-08-14T17:20:53+09:00",
                    "end_datetime": "2022-08-14T17:20:53+09:00",
                    "repeat_at": "string format invalid time.",
                    "process_after": "P1DT1H0M2.000000S",
                },
            },
        }
    ),
) -> dict[str, Any]:
    """概要

    詳細説明

    Args:

        item_id (UUID): ex)852d0bb1-6916-4107-a218-f4848e9e931f
        start_datetime (:obj:`引数(arg2)の型`, optional): ISO8601 isoformatを使うこと。

    Returns:

        dict[str, Any]: json format data.

    Raises:

        例外の名前: 例外の説明

    Python Examples:

        from uuid import uuid4
        from datetime import datetime, timedelta
        from zoneinfo import ZoneInfo
        from pydantic.json import timedelta_isoformat
        tzinfo=ZoneInfo("Asia/Tokyo")
        uuid4()
        # ミリ秒は切り捨て
        end_datetime = datetime.now(tzinfo).replace(microsecond = 0).isoformat()
        process_after =timedelta_isoformat(timedelta(hours=25, seconds=2))

    Bash Examples:

        uuid=$(uuidgen)
        # ミリ秒は切り捨て
        start_time=$(TZ=Asia/Tokyo date --iso-8601="seconds")
        curl -X 'PUT' \
            "http://127.0.0.1:8000/items/eee/${uuid}" \
            -H 'accept: application/json' \
            -H 'Content-Type: application/json' \
            -d '{
                "start_datetime": "2022-08-14T17:20:53+09:00",
                "end_datetime": "2022-08-14T17:20:53+09:00",
                "repeat_at": "14:23:55.003",
                "process_after": "P1DT1H0M2.000000S"
            }'

    Note:

        +があるため、URLエンコードに気をつけて、処理してください。

    """

    start_process = example_time.start_datetime + example_time.process_after
    duration = example_time.end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": example_time.start_datetime,
        "end_datetime": example_time.end_datetime,
        "repeat_at": example_time.repeat_at,
        "process_after": example_time.process_after,
        "start_process": start_process,
        "duration": duration,
    }
