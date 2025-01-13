from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd, AssetHive, AssetVest
from schemas.fields.resolvables import AnyAsset
from schemas.virtual_operation import VirtualOperation


class _ConsolidateTreasuryBalanceOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "consolidate_treasury_balance"
    __offset__ = 21

    total_moved: list[AnyAsset]


class ConsolidateTreasuryBalanceOperation(
    _ConsolidateTreasuryBalanceOperation
):
    ...


class ConsolidateTreasuryBalanceOperationLegacy(
    _ConsolidateTreasuryBalanceOperation
):
    ...
