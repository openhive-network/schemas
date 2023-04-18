from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pydantic import Field, Json

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import AccountName, CustomIdType


class CustomJsonOperation(PreconfiguredBaseModel):
    required_auths: list[AccountName]
    required_posting_auths: list[AccountName]
    id_: CustomIdType = Field(..., alias="id")
    json: Json[Any]
