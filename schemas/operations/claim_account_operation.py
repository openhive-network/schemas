from __future__ import annotations

from typing import Generic, Literal

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHive
from schemas.fields.basic import AccountName
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions

"""
If a user wants to pay a fee in RC fee should be equal 0.
"""


class _ClaimAccountOperation(Operation):
    __operation_name__ = "claim_account"
    __offset__ = 22

    creator: AccountName
    fee: AssetHive | Literal[0]
    extensions: FutureExtensions = Field(default_factory=FutureExtensions)


class ClaimAccountOperation(_ClaimAccountOperation):
    ...


class ClaimAccountOperationLegacy(_ClaimAccountOperation):
    ...
