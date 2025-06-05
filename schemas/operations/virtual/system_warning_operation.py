from __future__ import annotations

from schemas.virtual_operation import VirtualOperation


class SystemWarningOperation(VirtualOperation):
    message: str

    @classmethod
    def get_name(cls) -> str:
        return "system_warning"

    @classmethod
    def vop_offset(cls) -> int:
        return 32
