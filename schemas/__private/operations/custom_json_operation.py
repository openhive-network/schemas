from __future__ import annotations

from typing import Any

from pydantic import Field, Json

from schemas.__private.hive_fields_basic_schemas import AccountName, CustomIdType, EmptyString
from schemas.__private.preconfigured_base_model import Operation


class CustomJsonOperation(Operation):
    required_auths: list[AccountName]
    required_posting_auths: list[AccountName]
    id_: CustomIdType = Field(alias="id")
    json_: Json[Any] | EmptyString = Field(alias="json")
