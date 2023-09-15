from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName
from schemas.__private.virtual_operation import VirtualOperation


class ShutDownWitnessOperation(VirtualOperation):
    __operation_name__ = "shutdown_witness"

    owner: AccountName
