from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.assets.hive import AssetHiveHF26, AssetHiveLegacy, AssetHiveT
from schemas.fields.basic import AccountName
from schemas.fields.integers import Uint32t
from schemas.operation import Operation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _CollateralizedConvertOperation(Operation, GenericModel, Generic[AssetHiveT]):
    __operation_name__ = "collateralized_convert"
    __offset__ = 48

    owner: AccountName
    request_id: Uint32t = DEFAULT_REQUEST_ID
    amount: AssetHiveT


class CollateralizedConvertOperation(_CollateralizedConvertOperation[AssetHiveHF26]):
    ...


class CollateralizedConvertOperationLegacy(_CollateralizedConvertOperation[AssetHiveLegacy]):
    ...
