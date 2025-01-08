from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class _DhfFundingOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "dhf_funding"
    __offset__ = 17

    treasury: AccountName
    additional_funds: AssetHbd


class DhfFundingOperation(_DhfFundingOperation):
    pass


class DhfFundingOperationLegacy(_DhfFundingOperation):
    pass
