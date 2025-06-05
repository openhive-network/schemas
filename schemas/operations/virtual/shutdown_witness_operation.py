from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class ShutDownWitnessOperation(VirtualOperation):
    owner: AccountName

    @classmethod
    def get_name(cls) -> str:
        return "shutdown_witness"

    @classmethod
    def vop_offset(cls) -> int:
        return 8
