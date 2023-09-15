from __future__ import annotations

from schemas.__private.virtual_operation import VirtualOperation


class SystemWarningOperation(VirtualOperation):
    message: str
