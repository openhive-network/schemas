from __future__ import annotations

import msgspec

from schemas.fields.assets._base import AssetHive, AssetNaiAmount
from schemas.fields.basic import (
    AccountName,
    PublicKey,
    WitnessUrl,
)
from schemas.fields.compound import LegacyChainProperties
from schemas.operation import Operation


class _WitnessUpdateOperation(Operation):
    owner: AccountName
    url: WitnessUrl
    block_signing_key: PublicKey
    props: LegacyChainProperties
    fee: AssetHive | None

    @classmethod
    def get_name(cls) -> str:
        return "witness_update"

    @classmethod
    def offset(cls) -> int:
        return 11


class WitnessUpdateOperation(_WitnessUpdateOperation):
    fee: AssetHive = msgspec.field(default_factory=lambda: AssetHive(amount=AssetNaiAmount(0)))


class WitnessUpdateOperationLegacy(WitnessUpdateOperation):
    """Legacy operation model for witness update operations. Used for backwards compatibility."""
