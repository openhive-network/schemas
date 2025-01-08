from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHive
from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint32t
from schemas.operation import Operation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _CollateralizedConvertOperation(Operation, kw_only=True):
    __operation_name__ = "collateralized_convert"
    __offset__ = 48

    owner: AccountName
    requestid: Uint32t = DEFAULT_REQUEST_ID
    amount: AssetHive


class CollateralizedConvertOperation(_CollateralizedConvertOperation):
    ...


class CollateralizedConvertOperationLegacy(_CollateralizedConvertOperation):
    ...
