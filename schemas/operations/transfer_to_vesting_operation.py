from __future__ import annotations

from msgspec import field

from schemas.fields.assets._base import AssetHive
from schemas.fields.basic import AccountName, OptionallyEmptyAccountName
from schemas.operation import Operation


class _TransferToVestingOperation(Operation, kw_only=True):
    from_: AccountName = field(name="from")
    to: OptionallyEmptyAccountName
    amount: AssetHive

    @classmethod
    def get_name(cls) -> str:
        return "transfer_to_vesting"

    @classmethod
    def offset(cls) -> int:
        return 3


class TransferToVestingOperation(_TransferToVestingOperation):
    ...


class TransferToVestingOperationLegacy(_TransferToVestingOperation):
    ...
