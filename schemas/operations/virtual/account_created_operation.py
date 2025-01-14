from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetVest
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class _AccountCreatedOperation(VirtualOperation, kw_only=True):
    new_account_name: AccountName
    creator: AccountName
    initial_vesting_shares: AssetVest
    initial_delegation: AssetVest


    @classmethod
    def get_name(cls):
        return "account_created"
    
    @classmethod
    def offset(cls):
        return 30

class AccountCreatedOperation(_AccountCreatedOperation):
    ...


class AccountCreatedOperationLegacy(_AccountCreatedOperation):
    ...
