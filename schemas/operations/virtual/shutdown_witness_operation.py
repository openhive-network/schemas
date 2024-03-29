from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class ShutDownWitnessOperation(VirtualOperation):
    __operation_name__ = "shutdown_witness"
    __offset__ = 8

    owner: AccountName
