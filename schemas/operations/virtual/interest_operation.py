from __future__ import annotations

from typing import Final, Generic

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation
from pydantic import BaseModel

DEFAULT_IS_SAVED_INTO_HBD_BALANCE: Final[bool] = False


class _InterestOperation(VirtualOperation, BaseModel, Generic[AssetHbdT]):
    __operation_name__ = "interest"
    __offset__ = 5

    owner: AccountName
    interest: AssetHbdT
    is_saved_into_hbd_balance: bool = DEFAULT_IS_SAVED_INTO_HBD_BALANCE


class InterestOperation(_InterestOperation[AssetHbdHF26]):
    ...


class InterestOperationLegacy(_InterestOperation[AssetHbdLegacy]):
    ...
