from __future__ import annotations

from typing import Final, Generic

from pydantic.generics import GenericModel

from schemas.fields.basic import AccountName, AssetHiveHF26, AssetHiveLegacy, AssetHiveT, Uint32t
from schemas.operation import Operation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _CollateralizedConvertOperation(Operation, GenericModel, Generic[AssetHiveT]):
    __operation_name__ = "collateralized_convert"

    owner: AccountName
    request_id: Uint32t = DEFAULT_REQUEST_ID
    amount: AssetHiveT


class CollateralizedConvertOperation(_CollateralizedConvertOperation[AssetHiveHF26]):
    ...


class CollateralizedConvertOperationLegacy(_CollateralizedConvertOperation[AssetHiveLegacy]):
    ...
