from __future__ import annotations

from pydantic import Field

from schemas.fields.basic import AccountName
from schemas.fields.hex import Hex
from schemas.fields.integers import Uint16t
from schemas.operation import Operation


class CustomOperation(Operation, kw_only=True):
    __operation_name__ = "custom"
    __offset__ = 15

    required_auths: list[AccountName]
    id_: Uint16t = Field(alias="id")
    data: Hex
