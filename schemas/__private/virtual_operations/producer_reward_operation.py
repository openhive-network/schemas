from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHive, AssetVests
from schemas.__private.preconfigured_base_model import VirtualOperation


class ProducerRewardOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetVests]):
    producer: AccountName
    vesting_shares: AssetVests | AssetHive
