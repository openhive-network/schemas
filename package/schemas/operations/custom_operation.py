from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName, Uint16t


class CustomOperation(PreconfiguredBaseModel):
    required_auths: list[AccountName]
    id_: Uint16t = Field(..., alias="id")
    data: list[str]
