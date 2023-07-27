from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.hive_fields_basic_schemas import AccountName, AssetVests
from schemas.preconfigured_base_model import Operation


class DelegateVestingSharesOperation(Generic[AssetVests], GenericModel, Operation):
    delegator: AccountName
    delegatee: AccountName
    vesting_shares: AssetVests
