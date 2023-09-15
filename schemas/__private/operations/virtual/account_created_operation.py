from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetVests, AssetVestsHF26, AssetVestsLegacy
from schemas.__private.virtual_operation import VirtualOperation


class _AccountCreatedOperation(VirtualOperation, GenericModel, Generic[AssetVests]):
    __operation_name__ = "account_created"

    new_account_name: AccountName
    creator: AccountName
    initial_vesting_shares: AssetVests
    initial_delegation: AssetVests


class AccountCreatedOperationHF26(_AccountCreatedOperation[AssetVestsHF26]):
    ...


class AccountCreatedOperationLegacy(_AccountCreatedOperation[AssetVestsLegacy]):
    ...
