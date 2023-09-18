from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import (
    AccountName,
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
from schemas.operation import Operation


class _ClaimRewardBalanceOperation(Operation, GenericModel, Generic[AssetHiveT, AssetHbdT, AssetVestsT]):
    __operation_name__ = "claim_reward_balance"

    account: AccountName
    reward_hive: AssetHiveT
    reward_hbd: AssetHbdT
    reward_vests: AssetVestsT


class ClaimRewardBalanceOperation(_ClaimRewardBalanceOperation[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]):
    ...


class ClaimRewardBalanceOperationLegacy(
    _ClaimRewardBalanceOperation[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]
):
    ...
