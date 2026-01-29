from __future__ import annotations

from typing import Any

from msgspec import field

from schemas.fields.basic import AccountName, CustomIdType
from schemas.fields.resolvables import JsonString
from schemas.operation import Operation


class CustomJsonOperationGeneric(Operation):
    required_auths: list[AccountName]
    required_posting_auths: list[AccountName]
    id_: CustomIdType = field(name="id")
    json_: JsonString[Any] = field(name="json")

    @classmethod
    def get_name(cls) -> str:
        return "custom_json"

    @classmethod
    def offset(cls) -> int:
        return 18


CustomJsonOperation = CustomJsonOperationGeneric
