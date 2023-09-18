from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import (
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHbdT,
    AssetHiveHF26,
    AssetHiveLegacy,
    AssetHiveT,
    AssetVestsHF26,
    AssetVestsLegacy,
    AssetVestsT,
)
from schemas.virtual_operation import VirtualOperation


class _ConsolidateTreasuryBalanceOperation(VirtualOperation, GenericModel, Generic[AssetHiveT, AssetHbdT, AssetVestsT]):
    __operation_name__ = "consolidate_treasury_balance"

    total_moved: list[AssetHiveT | AssetHbdT | AssetVestsT]


class ConsolidateTreasuryBalanceOperation(
    _ConsolidateTreasuryBalanceOperation[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]
):
    ...


class ConsolidateTreasuryBalanceOperationLegacy(
    _ConsolidateTreasuryBalanceOperation[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]
):
    ...
