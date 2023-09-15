from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive, AssetVests
from schemas.__private.operation import Operation


class ClaimRewardBalanceOperation(Operation, GenericModel, Generic[AssetHive, AssetHbd, AssetVests]):
    account: AccountName
    reward_hive: AssetHive
    reward_hbd: AssetHbd
    reward_vests: AssetVests
