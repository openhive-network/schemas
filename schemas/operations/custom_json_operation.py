from __future__ import annotations

from pydantic import Field

from schemas.fields.basic import AccountName, CustomIdType
from schemas.fields.json_string import JsonString
from schemas.operation import Operation


class CustomJsonOperation(Operation):
    __operation_name__ = "custom_json"
    __offset__ = 18

    required_auths: list[AccountName]
    required_posting_auths: list[AccountName]
    id_: CustomIdType = Field(alias="id")
    json_: JsonString = Field(alias="json")
