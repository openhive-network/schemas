from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHive, AssetVest
from schemas.fields.basic import (
    AccountName,
    PublicKey,
)
from schemas.fields.compound import Authority
from schemas.operation import Operation


class _AccountCreateWithDelegationOperation(Operation):
    __operation_name__ = "account_create_with_delegation"
    __offset__ = 41

    fee: AssetHive
    delegation: AssetVest
    creator: AccountName
    new_account_name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: str


class AccountCreateWithDelegationOperation(_AccountCreateWithDelegationOperation):
    ...


class AccountCreateWithDelegationOperationLegacy(
    _AccountCreateWithDelegationOperation
):
    ...
