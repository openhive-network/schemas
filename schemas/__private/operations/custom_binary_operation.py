from __future__ import annotations

from pydantic import Field

from schemas.__private.hive_fields_basic_schemas import AccountName, Authority, CustomIdType
from schemas.__private.preconfigured_base_model import Operation


class CustomBinaryOperation(Operation):
    required_owner_auths: list[AccountName]
    required_active_auths: list[AccountName]
    required_posting_auths: list[AccountName]
    required_auths: list[Authority]
    id_: CustomIdType = Field(..., alias="id")
    data: list[str]
