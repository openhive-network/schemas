from __future__ import annotations

from typing import Generic, Literal

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import AccountName
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions

"""
If a user wants to pay a fee in RC fee should be equal 0.
"""


class _ClaimAccountOperation(Operation, GenericModel, Generic[AssetHiveT]):
    __operation_name__ = "claim_account"
    __offset__ = 22

    creator: AccountName
    fee: AssetHiveT | Literal[0]
    extensions: FutureExtensions = Field(default_factory=FutureExtensions)


class ClaimAccountOperation(_ClaimAccountOperation[AssetHiveHF26]):
    ...


class ClaimAccountOperationLegacy(_ClaimAccountOperation[AssetHiveLegacy]):
    ...
