from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_schemas import AccountName, AssetHive, Uint32t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class CollateralizedConvertOperation(PreconfiguredBaseModel, GenericModel, Generic[AssetHive]):
    owner: AccountName
    request_id: Uint32t = DEFAULT_REQUEST_ID
    amount: AssetHive
