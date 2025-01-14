from __future__ import annotations

from schemas.virtual_operation import VirtualOperation


class SystemWarningOperation(VirtualOperation):
    __operation_name__ = "system_warning"
    __offset__ = 32

    message: str

    @classmethod
    def get_name(cls):
        return "system_warning"
    
    @classmethod
    def offset(cls):
        return 32
