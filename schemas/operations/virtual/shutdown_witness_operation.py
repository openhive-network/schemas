from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class ShutDownWitnessOperation(VirtualOperation):
    owner: AccountName

    @classmethod
    def get_name(cls):
        return "shutdown_witness"
    
    @classmethod
    def offset(cls):
        return 8
