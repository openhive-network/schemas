from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHive, AssetHiveHF26, AssetHiveLegacy, Uint32t
from schemas.operation import Operation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _CollateralizedConvertOperation(Operation, GenericModel, Generic[AssetHive]):
    __operation_name__ = "collateralized_convert"

    owner: AccountName
    request_id: Uint32t = DEFAULT_REQUEST_ID
    amount: AssetHive


class CollateralizedConvertOperation(_CollateralizedConvertOperation[AssetHiveHF26]):
    ...


class CollateralizedConvertOperationLegacy(_CollateralizedConvertOperation[AssetHiveLegacy]):
    ...
