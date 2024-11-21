from __future__ import annotations

from typing import Final, Generic

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.virtual_operation import VirtualOperation
from pydantic import BaseModel

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _FillCollateralizedConvertRequestOperation(VirtualOperation, BaseModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "fill_collateralized_convert_request"
    __offset__ = 31

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
