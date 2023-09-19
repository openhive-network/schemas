from __future__ import annotations

from schemas._preconfigured_base_model import PreconfiguredBaseModel


class WalletDetails(PreconfiguredBaseModel):
    name: str
    unlocked: bool
