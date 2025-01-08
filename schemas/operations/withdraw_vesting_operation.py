from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetVest
from schemas.fields.basic import AccountName
from schemas.operation import Operation


class _WithdrawVestingOperation(Operation):
    __operation_name__ = "withdraw_vesting"
    __offset__ = 4

    account: AccountName
    vesting_shares: AssetVest


class WithdrawVestingOperation(_WithdrawVestingOperation):
    ...


class WithdrawVestingOperationLegacy(_WithdrawVestingOperation):
    ...
