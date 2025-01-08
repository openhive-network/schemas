from __future__ import annotations

from typing import Final

from schemas.fields.assets._base import AssetHbd, AssetHive
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.virtual_operation import VirtualOperation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _FillCollateralizedConvertRequestOperation(VirtualOperation, kw_only=True):
    owner: AccountName
    requestid: Uint32t = DEFAULT_REQUEST_ID
    amount_in: AssetHive
    amount_out: AssetHbd
    excess_collateral: AssetHive

    @classmethod
    def get_name(cls) -> str:
        return "fill_collateralized_convert_request"

    @classmethod
    def offset(cls) -> int:
        return 31


class FillCollateralizedConvertRequestOperation(_FillCollateralizedConvertRequestOperation):
    ...


class FillCollateralizedConvertRequestOperationLegacy(_FillCollateralizedConvertRequestOperation):
    ...
