from __future__ import annotations

from pydantic import Field

from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint16t
from schemas.operation import Operation


class CustomOperation(Operation):
    __operation_name__ = "custom"

    required_auths: list[AccountName]
    id_: Uint16t = Field(alias="id")
    data: list[str]
