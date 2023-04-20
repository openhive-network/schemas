from __future__ import annotations

from typing import Any

from pydantic import Field, Json

from schemas.__private.hive_fields_schemas_strict import AccountName, CustomIdType
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class CustomJsonOperation(PreconfiguredBaseModel):
    required_auths: list[AccountName]
    required_posting_auths: list[AccountName]
    id_: CustomIdType = Field(..., alias="id")
    json_: Json[Any] = Field(..., alias="json")
