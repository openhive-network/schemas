from __future__ import annotations

from pydantic import Field

from schemas.__private.hive_fields_basic_schemas import AccountName, Uint16t
from schemas.operation import Operation


class CustomOperation(Operation):
    __operation_name__ = "custom"

    required_auths: list[AccountName]
    id_: Uint16t = Field(alias="id")
    data: list[str]
