from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsLegacy, AssetVestsT
from schemas.virtual_operation import VirtualOperation


class _ConsolidateTreasuryBalanceOperation(VirtualOperation, GenericModel, Generic[AssetHiveT, AssetHbdT, AssetVestsT]):
    __operation_name__ = "consolidate_treasury_balance"
    __offset__ = 21

    total_moved: list[AssetHiveT | AssetHbdT | AssetVestsT]


class ConsolidateTreasuryBalanceOperation(
    _ConsolidateTreasuryBalanceOperation[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]
):
    ...


class ConsolidateTreasuryBalanceOperationLegacy(
    _ConsolidateTreasuryBalanceOperation[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]
):
    ...
