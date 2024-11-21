from __future__ import annotations

from typing import Generic

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation
from pydantic import BaseModel


class _DhfFundingOperation(VirtualOperation, BaseModel, Generic[AssetHbdT]):
    __operation_name__ = "dhf_funding"
    __offset__ = 17

    treasury: AccountName
    additional_funds: AssetHbdT


class DhfFundingOperation(_DhfFundingOperation[AssetHbdHF26]):
    pass


class DhfFundingOperationLegacy(_DhfFundingOperation[AssetHbdLegacy]):
    pass
