from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd, AssetHive, AssetVest
from schemas.fields.basic import AccountName
from schemas.operation import Operation


class _ClaimRewardBalanceOperation(Operation):
    __operation_name__ = "claim_reward_balance"
    __offset__ = 39

    account: AccountName
    reward_hive: AssetHive
    reward_hbd: AssetHbd
    reward_vests: AssetVest


class ClaimRewardBalanceOperation(_ClaimRewardBalanceOperation):
    ...


class ClaimRewardBalanceOperationLegacy(
    _ClaimRewardBalanceOperation
):
    ...
