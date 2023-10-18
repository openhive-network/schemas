from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class ProducerMissedOperation(VirtualOperation):
    __operation_name__ = "producer_missed"
    __offset__ = 36

    producer: AccountName
