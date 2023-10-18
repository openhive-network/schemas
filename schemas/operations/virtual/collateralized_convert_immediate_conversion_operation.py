from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.virtual_operation import VirtualOperation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _CollateralizedConvertImmediateConversionOperation(VirtualOperation, GenericModel, Generic[AssetHbdT]):
    __operation_name__ = "collateralized_convert_immediate_conversion"
    __offset__ = 38

    owner: AccountName
    requestid: Uint32t = DEFAULT_REQUEST_ID
    hbd_out: AssetHbdT


class CollateralizedConvertImmediateConversionOperation(
    _CollateralizedConvertImmediateConversionOperation[AssetHbdHF26]
):
    ...


class CollateralizedConvertImmediateConversionOperationLegacy(
    _CollateralizedConvertImmediateConversionOperation[AssetHbdLegacy]
):
    ...
