from __future__ import annotations

from typing import Final

from schemas.fields.assets._base import AssetHbd
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.virtual_operation import VirtualOperation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _CollateralizedConvertImmediateConversionOperation(VirtualOperation, kw_only=True):
    owner: AccountName
    requestid: Uint32t = DEFAULT_REQUEST_ID
    hbd_out: AssetHbd

    @classmethod
    def get_name(cls) -> str:
        return "collateralized_convert_immediate_conversion"

    @classmethod
    def vop_offset(cls) -> int:
        return 38


class CollateralizedConvertImmediateConversionOperation(_CollateralizedConvertImmediateConversionOperation):
    ...


class CollateralizedConvertImmediateConversionOperationLegacy(_CollateralizedConvertImmediateConversionOperation):
    ...
