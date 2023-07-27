from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.hive_fields_basic_schemas import AccountName, AssetHive, AssetVests
from schemas.preconfigured_base_model import VirtualOperation


class PowRewardOperation(Generic[AssetHive, AssetVests], GenericModel, VirtualOperation):
    worker: AccountName
    reward: AssetHive | AssetVests
