from __future__ import annotations

from typing import Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHive
from schemas.fields.basic import (
    AccountName,
    EmptyString,
)
from schemas.operation import Operation


class _TransferToVestingOperation(Operation, kw_only=True):
    __operation_name__ = "transfer_to_vesting"
    __offset__ = 3

    from_: AccountName = Field(alias="from")
    to: AccountName | EmptyString
    amount: AssetHive


class TransferToVestingOperation(_TransferToVestingOperation):
    ...


class TransferToVestingOperationLegacy(_TransferToVestingOperation):
    ...
