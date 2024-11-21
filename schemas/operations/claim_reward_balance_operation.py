from __future__ import annotations

from typing import Generic

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsLegacy, AssetVestsT
from schemas.fields.basic import AccountName
from schemas.operation import Operation
from pydantic import BaseModel


class _ClaimRewardBalanceOperation(Operation, BaseModel, Generic[AssetHiveT, AssetHbdT, AssetVestsT]):
    __operation_name__ = "claim_reward_balance"
    __offset__ = 39

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
