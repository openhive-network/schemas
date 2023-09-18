from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName
from schemas.virtual_operation import VirtualOperation


class ProducerMissedOperation(VirtualOperation):
    __operation_name__ = "producer_missed"

    producer: AccountName
