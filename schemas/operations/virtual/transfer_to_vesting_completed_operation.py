from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import (
    AccountName,
    AssetHive,
    AssetHiveHF26,
    AssetHiveLegacy,
    AssetVests,
    AssetVestsHF26,
    AssetVestsLegacy,
)
from schemas.virtual_operation import VirtualOperation


class _TransferToVestingCompletedOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetVests]):
    __operation_name__ = "transfer_to_vesting_completed"

    from_account: AccountName
    to_account: AccountName
    hive_vested: AssetHive
    vesting_shares_received: AssetVests


class TransferToVestingCompletedOperation(_TransferToVestingCompletedOperation[AssetHiveHF26, AssetVestsHF26]):
    ...


class TransferToVestingCompletedOperationLegacy(
    _TransferToVestingCompletedOperation[AssetHiveLegacy, AssetVestsLegacy]
):
    ...
