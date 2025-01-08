from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets._base import AssetHbd, AssetHive

from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.virtual_operation import VirtualOperation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _FillCollateralizedConvertRequestOperation(VirtualOperation, kw_only=True):
    __operation_name__ = "fill_collateralized_convert_request"
    __offset__ = 31

    owner: AccountName
    requestid: Uint32t = DEFAULT_REQUEST_ID
    amount_in: AssetHive
    amount_out: AssetHbd
    excess_collateral: AssetHive


class FillCollateralizedConvertRequestOperation(
    _FillCollateralizedConvertRequestOperation
):
    ...


class FillCollateralizedConvertRequestOperationLegacy(
    _FillCollateralizedConvertRequestOperation
):
    ...
