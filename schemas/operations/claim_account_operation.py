from __future__ import annotations

from typing import Generic, Literal

from pydantic.generics import GenericModel

from schemas.fields.basic import AccountName, AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.operation import Operation

"""
If a user wants to pay a fee in RC fee should be equal 0.
"""


class _ClaimAccountOperation(Operation, GenericModel, Generic[AssetHiveT]):
    __operation_name__ = "claim_account"

    creator: AccountName
    fee: AssetHiveT | Literal[0]


class ClaimAccountOperation(_ClaimAccountOperation[AssetHiveHF26]):
    ...


class ClaimAccountOperationLegacy(_ClaimAccountOperation[AssetHiveLegacy]):
    ...
