from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import (
    AccountName,
)
from schemas.fields.integers import Uint32t
from schemas.virtual_operation import VirtualOperation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _FillConvertRequestOperation(VirtualOperation, GenericModel, Generic[AssetHiveT, AssetHbdT]):
    __operation_name__ = "fill_convert_request"
    __offset__ = 0

    owner: AccountName
    requestid: Uint32t = DEFAULT_REQUEST_ID
    amount_in: AssetHbdT
    amount_out: AssetHiveT


class FillConvertRequestOperation(_FillConvertRequestOperation[AssetHiveHF26, AssetHbdHF26]):
    ...


class FillConvertRequestOperationLegacy(_FillConvertRequestOperation[AssetHiveLegacy, AssetHbdLegacy]):
    ...
