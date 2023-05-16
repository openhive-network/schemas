from __future__ import annotations

from pydantic import Field

from schemas.__private.hive_fields_basic_schemas import AccountName, Uint16t
from schemas.__private.preconfigured_base_model import Operation


class CustomOperation(Operation):
    required_auths: list[AccountName]
    id_: Uint16t = Field(..., alias="id")
    data: list[str]
