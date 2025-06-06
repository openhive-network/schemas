from __future__ import annotations

from typing import Final

from msgspec import field

from schemas.fields.assets._base import AssetHbd, AssetHive
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.integers import Uint32t
from schemas.fields.resolvables import AssetUnionAssetHiveAssetHbd
from schemas.operation import Operation

DEFAULT_ESCROW_ID: Final[Uint32t] = Uint32t(30)


class EscrowTransferOperation(Operation, kw_only=True):
    from_: AccountName = field(name="from")
    to: AccountName
    agent: AccountName
    escrow_id: Uint32t = DEFAULT_ESCROW_ID
    hbd_amount: AssetHbd
    hive_amount: AssetHive
    fee: AssetUnionAssetHiveAssetHbd
    ratification_deadline: HiveDateTime
    escrow_expiration: HiveDateTime
    json_meta: str

    @classmethod
    def get_name(cls) -> str:
        return "escrow_transfer"

    @classmethod
    def offset(cls) -> int:
        return 27
