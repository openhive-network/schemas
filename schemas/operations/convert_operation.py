from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd
from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint32t
from schemas.operation import Operation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _ConvertOperation(Operation, kw_only=True):
    __operation_name__ = "convert"
    __offset__ = 8

    owner: AccountName
    requestid: Uint32t = DEFAULT_REQUEST_ID
    amount: AssetHbd


class ConvertOperation(_ConvertOperation):
    ...


class ConvertOperationLegacy(_ConvertOperation):
    ...
