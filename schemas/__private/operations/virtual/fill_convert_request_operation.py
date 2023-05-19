from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHbd, AssetHive, Uint32t
from schemas.__private.preconfigured_base_model import VirtualOperation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class FillConvertRequestOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetHbd]):
    owner: AccountName
    request_id: Uint32t = DEFAULT_REQUEST_ID
    amount_in: AssetHbd
    amount_out: AssetHive
