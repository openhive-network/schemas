from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetVests, AssetVestsHF26, AssetVestsLegacy
from schemas.__private.operation import Operation


class _WithdrawVestingOperation(Operation, GenericModel, Generic[AssetVests]):
    __operation_name__ = "withdraw_vesting"

    account: AccountName
    vesting_shares: AssetVests


class WithdrawVestingOperationHF26(_WithdrawVestingOperation[AssetVestsHF26]):
    ...


class WithdrawVestingOperationLegacy(_WithdrawVestingOperation[AssetVestsLegacy]):
    ...
