from __future__ import annotations

from pydantic import Field

from schemas.__private.hive_fields_schemas_strict import AccountName, Uint16t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class CustomOperation(PreconfiguredBaseModel):
    required_auths: list[AccountName]
    id_: Uint16t = Field(..., alias="id")
    data: list[str]
