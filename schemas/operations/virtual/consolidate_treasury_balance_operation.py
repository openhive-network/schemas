from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AssetHbd,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHive,
    AssetHiveHF26,
    AssetHiveLegacy,
    AssetVests,
    AssetVestsHF26,
    AssetVestsLegacy,
)
from schemas.virtual_operation import VirtualOperation


class _ConsolidateTreasuryBalanceOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetHbd, AssetVests]):
    __operation_name__ = "consolidate_treasury_balance"

    total_moved: list[AssetHive | AssetHbd | AssetVests]


class ConsolidateTreasuryBalanceOperation(
    _ConsolidateTreasuryBalanceOperation[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]
):
    ...


class ConsolidateTreasuryBalanceOperationLegacy(
    _ConsolidateTreasuryBalanceOperation[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]
):
    ...
