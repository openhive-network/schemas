from __future__ import annotations

from typing import Generic, Literal

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHive, AssetHiveHF26, AssetHiveLegacy
from schemas.__private.operation import Operation

"""
If a user wants to pay a fee in RC fee should be equal 0.
"""


class _ClaimAccountOperation(Operation, GenericModel, Generic[AssetHive]):
    __operation_name__ = "claim_account"

    creator: AccountName
    fee: AssetHive | Literal[0]


class ClaimAccountOperation(_ClaimAccountOperation[AssetHiveHF26]):
    ...


class ClaimAccountOperationLegacy(_ClaimAccountOperation[AssetHiveLegacy]):
    ...
