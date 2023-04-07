from __future__ import annotations

from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, CustomIdType, Authority


class CustomBinaryOperation(BaseModel, extra=Extra.forbid):
    required_owner_auths: list[AccountName]
    required_active_auths: list[AccountName]
    required_posting_auths: list[AccountName]
    required_auths: list[Authority]
    id: CustomIdType
    data: list[str]

