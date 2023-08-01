from __future__ import annotations

from schemas.__private.preconfigured_base_model import VirtualOperation


class SystemWarningOperation(VirtualOperation):
    message: str
