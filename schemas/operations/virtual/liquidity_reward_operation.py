from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.hive_fields_basic_schemas import AccountName, AssetHive
from schemas.preconfigured_base_model import VirtualOperation


class LiquidityRewardOperation(Generic[AssetHive], GenericModel, VirtualOperation):
    owner: AccountName
    payout: AssetHive
