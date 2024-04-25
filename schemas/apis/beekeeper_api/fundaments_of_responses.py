from __future__ import annotations

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.basic import PublicKey


class WalletDetails(PreconfiguredBaseModel):
    name: str
    unlocked: bool


class PublicKeyItem(PreconfiguredBaseModel):
    public_key: PublicKey
