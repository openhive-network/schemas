from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class ProducerMissedOperation(VirtualOperation):
    __operation_name__ = "producer_missed"

    producer: AccountName
