from __future__ import annotations

from msgspec import field

from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.resolvables import AssetUnionAssetHiveAssetHbd
from schemas.operation import Operation


class _TransferToSavingsOperation(Operation, kw_only=True):
    from_: AccountName = field(name="from")
    to: AccountName
    amount: AssetUnionAssetHiveAssetHbd
    memo: str

    @classmethod
    def get_name(cls) -> str:
        return "transfer_to_savings"

    @classmethod
    def offset(cls) -> int:
        return 32


class TransferToSavingsOperation(_TransferToSavingsOperation):
    ...


class TransferToSavingsOperationLegacy(_TransferToSavingsOperation):
    ...
