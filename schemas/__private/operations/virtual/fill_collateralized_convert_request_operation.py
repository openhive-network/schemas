from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive, Uint32t
from schemas.__private.preconfigured_base_model import VirtualOperation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class FillCollateralizedConvertRequestOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetHbd]):
    owner: AccountName
    requestid: Uint32t = DEFAULT_REQUEST_ID
    amount_in: AssetHive
    amount_out: AssetHbd
    excess_collateral: AssetHive
