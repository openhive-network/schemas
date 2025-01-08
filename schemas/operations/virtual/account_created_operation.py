from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetVest
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class _AccountCreatedOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "account_created"
    __offset__ = 30

    new_account_name: AccountName
    creator: AccountName
    initial_vesting_shares: AssetVest
    initial_delegation: AssetVest


class AccountCreatedOperation(_AccountCreatedOperation):
    ...


class AccountCreatedOperationLegacy(_AccountCreatedOperation):
    ...
