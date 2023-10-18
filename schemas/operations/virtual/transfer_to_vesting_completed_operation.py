from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsLegacy, AssetVestsT
from schemas.fields.basic import (
    AccountName,
)
from schemas.virtual_operation import VirtualOperation


class _TransferToVestingCompletedOperation(VirtualOperation, GenericModel, Generic[AssetHiveT, AssetVestsT]):
    __operation_name__ = "transfer_to_vesting_completed"
    __offset__ = 27

    from_account: AccountName
    to_account: AccountName
    hive_vested: AssetHiveT
    vesting_shares_received: AssetVestsT


class TransferToVestingCompletedOperation(_TransferToVestingCompletedOperation[AssetHiveHF26, AssetVestsHF26]):
    ...


class TransferToVestingCompletedOperationLegacy(
    _TransferToVestingCompletedOperation[AssetHiveLegacy, AssetVestsLegacy]
):
    ...
