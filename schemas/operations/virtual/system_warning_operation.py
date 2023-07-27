from __future__ import annotations

from schemas.preconfigured_base_model import VirtualOperation


class SystemWarningOperation(VirtualOperation):
    message: str
