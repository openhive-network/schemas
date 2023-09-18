from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.vests import AssetVestsHF26, AssetVestsLegacy, AssetVestsT
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class _AccountCreatedOperation(VirtualOperation, GenericModel, Generic[AssetVestsT]):
    __operation_name__ = "account_created"

    new_account_name: AccountName
    creator: AccountName
    initial_vesting_shares: AssetVestsT
    initial_delegation: AssetVestsT


class AccountCreatedOperation(_AccountCreatedOperation[AssetVestsHF26]):
    ...


class AccountCreatedOperationLegacy(_AccountCreatedOperation[AssetVestsLegacy]):
    ...
