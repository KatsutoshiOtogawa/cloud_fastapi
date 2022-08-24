""" This is a program"""

from typing import Any, Optional
from uuid import UUID
from datetime import datetime, time, timedelta
from fastapi import APIRouter, Path, Body
from pydantic import BaseModel, Field

# userのrouter
router = APIRouter()

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
@router.put("/items/eee/{item_id}", tags=["time_example"])
async def read_items(
    item_id: UUID = Path(
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** Example time works correctly.",
                "value": "852d0bb1-6916-4107-a218-f4848e9e931f",
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "description": "Fast API can convert price `strings` to actual `numbers` automatical",
                "value": "invalid str string",
            },
        }
    ),
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
