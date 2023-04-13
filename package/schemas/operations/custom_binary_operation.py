from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName, CustomIdType, Authority
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class CustomBinaryOperation(PreconfiguredBaseModel):
    required_owner_auths: list[AccountName]
    required_active_auths: list[AccountName]
    required_posting_auths: list[AccountName]
    required_auths: list[Authority]
    id: CustomIdType
    data: list[str]
