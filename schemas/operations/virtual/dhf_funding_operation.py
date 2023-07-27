from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.hive_fields_basic_schemas import AccountName, AssetHbd
from schemas.preconfigured_base_model import VirtualOperation


class DhfFundingOperation(Generic[AssetHbd], GenericModel, VirtualOperation):
    treasury: AccountName
    additional_funds: AssetHbd
