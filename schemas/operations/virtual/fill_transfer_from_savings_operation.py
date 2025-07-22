from __future__ import annotations

from typing import Final

from msgspec import field

from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.fields.resolvables import AssetUnionAssetHiveAssetHbd
from schemas.virtual_operation import VirtualOperation

DEFAULT_REQUEST_ID: Final[Uint32t] = 0


class FillTransferFromSavingsOperation(VirtualOperation, kw_only=True):
    from_: AccountName = field(name="from")
    to: AccountName
    amount: AssetUnionAssetHiveAssetHbd
    request_id: Uint32t = DEFAULT_REQUEST_ID
    memo: str

    @classmethod
    def get_name(cls) -> str:
        return "fill_transfer_from_savings"

    @classmethod
    def vop_offset(cls) -> int:
        return 9
