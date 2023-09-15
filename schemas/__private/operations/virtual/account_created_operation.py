from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetVests
from schemas.__private.virtual_operation import VirtualOperation


class AccountCreatedOperation(VirtualOperation, GenericModel, Generic[AssetVests]):
    new_account_name: AccountName
    creator: AccountName
    initial_vesting_shares: AssetVests
    initial_delegation: AssetVests
