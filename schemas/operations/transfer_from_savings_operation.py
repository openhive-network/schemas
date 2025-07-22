from __future__ import annotations

from typing import Final

from msgspec import field

from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.fields.resolvables import AssetUnionAssetHiveAssetHbd
from schemas.operation import Operation

DEFAULT_TYPE_ID: Final[Uint32t] = 0


class TransferFromSavingsOperation(Operation, kw_only=True):
    from_: AccountName = field(name="from")
    to: AccountName
    request_id: Uint32t = DEFAULT_TYPE_ID
    amount: AssetUnionAssetHiveAssetHbd
    memo: str

    @classmethod
    def get_name(cls) -> str:
        return "transfer_from_savings"

    @classmethod
    def offset(cls) -> int:
        return 33
