from __future__ import annotations

from msgspec import field

from schemas.fields.assets._base import AssetHbd, AssetHive
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.resolvables import AssetUnion
from schemas.operation import Operation


class _TransferOperation(Operation, kw_only=True):
    from_: AccountName = field(name="from")
    to: AccountName
    amount: AssetUnion[AssetHive, AssetHbd]
    memo: str

    @classmethod
    def get_name(cls) -> str:
        return "transfer"

    @classmethod
    def offset(cls) -> int:
        return 2


class TransferOperation(_TransferOperation):
    ...


class TransferOperationLegacy(_TransferOperation):
    ...
