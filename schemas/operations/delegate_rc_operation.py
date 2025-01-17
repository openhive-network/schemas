from __future__ import annotations


from schemas.fields.basic import AccountName
from schemas.operations.custom.custom_base_operation import CustomBaseOperation

from msgspec import field

class DelegateRcOperation(CustomBaseOperation):
    __operation_name__ = "delegate_rc"

    from_: AccountName = field(name="from")
    delegatees: list[AccountName]
    max_rc: int

    @classmethod
    def get_name(cls):
        return "delegate_rc"
