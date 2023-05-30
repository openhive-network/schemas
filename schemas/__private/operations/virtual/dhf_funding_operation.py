from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd
from schemas.__private.preconfigured_base_model import VirtualOperation


class DhfFundingOperation(Generic[AssetHbd], GenericModel, VirtualOperation):
    treasury: AccountName
    additional_funds: AssetHbd
