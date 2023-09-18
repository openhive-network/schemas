from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import (
    AccountName,
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
from schemas.operation import Operation


class _ClaimRewardBalanceOperation(Operation, GenericModel, Generic[AssetHive, AssetHbd, AssetVests]):
    __operation_name__ = "claim_reward_balance"

    account: AccountName
    reward_hive: AssetHive
    reward_hbd: AssetHbd
    reward_vests: AssetVests


class ClaimRewardBalanceOperation(_ClaimRewardBalanceOperation[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]):
    ...


class ClaimRewardBalanceOperationLegacy(
    _ClaimRewardBalanceOperation[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]
):
    ...
