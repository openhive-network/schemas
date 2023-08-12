from __future__ import annotations

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class WalletDetails(PreconfiguredBaseModel):
    name: str
    unlocked: bool
