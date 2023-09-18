from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import (
    AccountName,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHbdT,
    AssetHiveHF26,
    AssetHiveLegacy,
    AssetHiveT,
    Uint32t,
)
from schemas.virtual_operation import VirtualOperation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _FillCollateralizedConvertRequestOperation(VirtualOperation, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "fill_collateralized_convert_request"

    owner: AccountName
    requestid: Uint32t = DEFAULT_REQUEST_ID
    amount_in: AssetHiveT
    amount_out: AssetHbdT
    excess_collateral: AssetHiveT


class FillCollateralizedConvertRequestOperation(
    _FillCollateralizedConvertRequestOperation[AssetHiveHF26, AssetHbdHF26]
):
    ...


class FillCollateralizedConvertRequestOperationLegacy(
    _FillCollateralizedConvertRequestOperation[AssetHiveLegacy, AssetHbdLegacy]
):
    ...
