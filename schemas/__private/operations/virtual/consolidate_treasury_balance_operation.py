from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AssetHbd, AssetHive, AssetVests
from schemas.__private.preconfigured_base_model import VirtualOperation


class ConsolidateTreasuryBalanceOperation(Generic[AssetHive, AssetHbd, AssetVests], GenericModel, VirtualOperation):
    total_moved: list[AssetHive | AssetHbd | AssetVests]