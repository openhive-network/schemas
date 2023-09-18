from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import (
    AccountName,
    AssetHbd,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHive,
    AssetHiveHF26,
    AssetHiveLegacy,
    Uint32t,
)
from schemas.virtual_operation import VirtualOperation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _FillCollateralizedConvertRequestOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetHbd]):
    __operation_name__ = "fill_collateralized_convert_request"

    owner: AccountName
    requestid: Uint32t = DEFAULT_REQUEST_ID
    amount_in: AssetHive
    amount_out: AssetHbd
    excess_collateral: AssetHive


class FillCollateralizedConvertRequestOperation(
    _FillCollateralizedConvertRequestOperation[AssetHiveHF26, AssetHbdHF26]
):
    ...


class FillCollateralizedConvertRequestOperationLegacy(
    _FillCollateralizedConvertRequestOperation[AssetHiveLegacy, AssetHbdLegacy]
):
    ...
