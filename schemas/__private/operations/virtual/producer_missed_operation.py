from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName
from schemas.__private.preconfigured_base_model import VirtualOperation


class ProducerMissedOperation(VirtualOperation):
    producer: AccountName
