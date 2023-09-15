from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd
from schemas.__private.virtual_operation import VirtualOperation


class DhfFundingOperation(VirtualOperation, GenericModel, Generic[AssetHbd]):
    treasury: AccountName
    additional_funds: AssetHbd
