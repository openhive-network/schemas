from __future__ import annotations

from pydantic import Field

from schemas.fields.basic import AccountName
from schemas.operations.custom.custom_base_operation import CustomBaseOperation


class DelegateRcOperation(CustomBaseOperation):
    __operation_name__ = "delegate_rc"

    from_: AccountName = Field(alias="from")
    delegatees: list[AccountName]
    max_rc: int
