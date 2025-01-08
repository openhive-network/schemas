from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHive, AssetVest

from schemas.fields.basic import (
    AccountName,
)
from schemas.virtual_operation import VirtualOperation


class _TransferToVestingCompletedOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "transfer_to_vesting_completed"
    __offset__ = 27

    from_account: AccountName
    to_account: AccountName
    hive_vested: AssetHive
    vesting_shares_received: AssetVest


class TransferToVestingCompletedOperation(_TransferToVestingCompletedOperation):
    ...


class TransferToVestingCompletedOperationLegacy(
    _TransferToVestingCompletedOperation
):
    ...
