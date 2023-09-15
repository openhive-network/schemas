from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AssetHbd, AssetHive, AssetVests
from schemas.__private.virtual_operation import VirtualOperation


class ClearNullAccountBalanceOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetHbd, AssetVests]):
    total_cleared: list[AssetHive | AssetHbd | AssetVests]
