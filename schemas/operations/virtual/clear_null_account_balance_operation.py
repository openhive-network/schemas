from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsLegacy, AssetVestsT
from schemas.virtual_operation import VirtualOperation


class _ClearNullAccountBalanceOperation(VirtualOperation, GenericModel, Generic[AssetHiveT, AssetHbdT, AssetVestsT]):
    __operation_name__ = "clear_null_account_balance"
    __offset__ = 15

    total_cleared: list[AssetHiveT | AssetHbdT | AssetVestsT]


class ClearNullAccountBalanceOperation(_ClearNullAccountBalanceOperation[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]):
    ...


class ClearNullAccountBalanceOperationLegacy(
    _ClearNullAccountBalanceOperation[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]
):
    ...
