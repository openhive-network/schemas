from __future__ import annotations

from typing import Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHive
from schemas.fields.basic import (
    AccountName,
    EmptyString,
)
from schemas.fields.resolvables import OptionallyEmpty
from schemas.operation import Operation


class _TransferToVestingOperation(Operation, kw_only=True):
    from_: AccountName = Field(alias="from")
    to: OptionallyEmpty[AccountName]
    amount: AssetHive


    @classmethod
    def get_name(cls):
        return "transfer_to_vesting"
    
    @classmethod
    def offset(cls):
        return 3

class TransferToVestingOperation(_TransferToVestingOperation):
    ...


class TransferToVestingOperationLegacy(_TransferToVestingOperation):
    ...
