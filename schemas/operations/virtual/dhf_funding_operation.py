from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import AccountName, AssetHbd, AssetHbdHF26, AssetHbdLegacy
from schemas.virtual_operation import VirtualOperation


class _DhfFundingOperation(VirtualOperation, GenericModel, Generic[AssetHbd]):
    __operation_name__ = "dhf_funding"

    treasury: AccountName
    additional_funds: AssetHbd


class DhfFundingOperation(_DhfFundingOperation[AssetHbdHF26]):
    pass


class DhfFundingOperationLegacy(_DhfFundingOperation[AssetHbdLegacy]):
    pass
