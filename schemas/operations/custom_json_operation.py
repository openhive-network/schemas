from __future__ import annotations

import json
from typing import Any

from pydantic import Field, validator

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import AccountName, CustomIdType
from schemas.operation import Operation


class CustomJsonOperation(Operation):
    __operation_name__ = "custom_json"
    __offset__ = 18

    required_auths: list[AccountName]
    required_posting_auths: list[AccountName]
    id_: CustomIdType = Field(alias="id")
    json_: str = Field(alias="json")

    @validator("json_", pre=True)
    @classmethod
    def json_string(cls, obj: Any) -> str:
        if isinstance(obj, PreconfiguredBaseModel):
            return obj.json(by_alias=True)
        if isinstance(obj, dict | list):
            return json.dumps(obj)
        return str(obj)
