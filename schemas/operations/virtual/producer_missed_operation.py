from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class ProducerMissedOperation(VirtualOperation):
    producer: AccountName

    @classmethod
    def get_name(cls) -> str:
        return "producer_missed"

    @classmethod
    def offset(cls) -> int:
        return 36
