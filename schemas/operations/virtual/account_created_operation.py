from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.hive_fields_basic_schemas import AccountName, AssetVests
from schemas.preconfigured_base_model import VirtualOperation


class AccountCreatedOperation(Generic[AssetVests], GenericModel, VirtualOperation):
    new_account_name: AccountName
    creator: AccountName
    initial_vesting_shares: AssetVests
    initial_delegation: AssetVests
