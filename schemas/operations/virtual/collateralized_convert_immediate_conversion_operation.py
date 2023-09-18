from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import (
    AccountName,
    AssetHbd,
    AssetHbdHF26,
    AssetHbdLegacy,
    Uint32t,
)
from schemas.virtual_operation import VirtualOperation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _CollateralizedConvertImmediateConversionOperation(VirtualOperation, GenericModel, Generic[AssetHbd]):
    __operation_name__ = "collateralized_convert_immediate_conversion"

    owner: AccountName
    requestid: Uint32t = DEFAULT_REQUEST_ID
    hbd_out: AssetHbd


class CollateralizedConvertImmediateConversionOperation(
    _CollateralizedConvertImmediateConversionOperation[AssetHbdHF26]
):
    ...


class CollateralizedConvertImmediateConversionOperationLegacy(
    _CollateralizedConvertImmediateConversionOperation[AssetHbdLegacy]
):
    ...
