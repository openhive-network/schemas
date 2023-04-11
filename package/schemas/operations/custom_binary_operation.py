from __future__ import annotations

from schemas.package.schemas.predefined import AccountName, CustomIdType, Authority
from preconfigure_base_model import PreconfiguredBaseModel


class CustomBinaryOperation(PreconfiguredBaseModel):
    required_owner_auths: list[AccountName]
    required_active_auths: list[AccountName]
    required_posting_auths: list[AccountName]
    required_auths: list[Authority]
    id: CustomIdType
    data: list[str]

