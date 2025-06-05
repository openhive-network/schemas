from __future__ import annotations

from msgspec import field

from schemas.fields.basic import AccountName
from schemas.operations.custom.custom_base_operation import CustomBaseOperation


class DelegateRcOperation(CustomBaseOperation):
    __operation_name__ = "delegate_rc"

    from_: AccountName = field(name="from")
    delegatees: list[AccountName]
    max_rc: int

    @classmethod
    def get_name(cls) -> str:
        return "delegate_rc"
