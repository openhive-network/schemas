from __future__ import annotations

from schemas.__private.virtual_operation import VirtualOperation


class SystemWarningOperation(VirtualOperation):
    __operation_name__ = "system_warning"

    message: str
