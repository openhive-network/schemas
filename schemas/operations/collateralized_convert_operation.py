from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.hive_fields_basic_schemas import AccountName, AssetHive, Uint32t
from schemas.preconfigured_base_model import Operation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class CollateralizedConvertOperation(Generic[AssetHive], GenericModel, Operation):
    owner: AccountName
    request_id: Uint32t = DEFAULT_REQUEST_ID
    amount: AssetHive
