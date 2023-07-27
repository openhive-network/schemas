from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.hive_fields_basic_schemas import AccountName, AssetHbd, Uint32t
from schemas.preconfigured_base_model import VirtualOperation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class CollateralizedConvertImmediateConversionOperation(Generic[AssetHbd], GenericModel, VirtualOperation):
    owner: AccountName
    requestid: Uint32t = DEFAULT_REQUEST_ID
    hbd_out: AssetHbd
