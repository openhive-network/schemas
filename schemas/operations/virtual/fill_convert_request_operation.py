from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import (
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


class _FillConvertRequestOperation(VirtualOperation, GenericModel, Generic[AssetHive, AssetHbd]):
    __operation_name__ = "fill_convert_request"

    owner: AccountName
    request_id: Uint32t = DEFAULT_REQUEST_ID
    amount_in: AssetHbd
    amount_out: AssetHive


class FillConvertRequestOperation(_FillConvertRequestOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class FillConvertRequestOperationLegacy(_FillConvertRequestOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
