from __future__ import annotations

from typing import Final, Generic

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint32t
from schemas.operation import Operation
from pydantic import BaseModel

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _ConvertOperation(Operation, BaseModel, Generic[AssetHbdT]):
    __operation_name__ = "convert"
    __offset__ = 8

    owner: AccountName
    requestid: Uint32t = DEFAULT_REQUEST_ID
    amount: AssetHbdT


class ConvertOperation(_ConvertOperation[AssetHbdHF26]):
    ...


class ConvertOperationLegacy(_ConvertOperation[AssetHbdLegacy]):
    ...
