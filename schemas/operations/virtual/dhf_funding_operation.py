from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class _DhfFundingOperation(VirtualOperation, GenericModel, Generic[AssetHbdT]):
    __operation_name__ = "dhf_funding"

    treasury: AccountName
    additional_funds: AssetHbdT


class DhfFundingOperation(_DhfFundingOperation[AssetHbdHF26]):
    pass


class DhfFundingOperationLegacy(_DhfFundingOperation[AssetHbdLegacy]):
    pass
