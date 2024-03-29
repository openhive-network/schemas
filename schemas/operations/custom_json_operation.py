from __future__ import annotations

from typing import Any

from pydantic import Field, Json

from schemas.fields.basic import AccountName, CustomIdType, EmptyString
from schemas.operation import Operation


class CustomJsonOperation(Operation):
    __operation_name__ = "custom_json"
    __offset__ = 18

    required_auths: list[AccountName]
    required_posting_auths: list[AccountName]
    id_: CustomIdType = Field(alias="id")
    json_: Json[Any] | EmptyString = Field(alias="json")
