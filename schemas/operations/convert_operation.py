from __future__ import annotations

from typing import Final, Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.assets.hbd import AssetHbdHF26, AssetHbdLegacy, AssetHbdT
from schemas.fields.basic import AccountName, Uint32t
from schemas.operation import Operation

DEFAULT_REQUEST_ID: Final[Uint32t] = Uint32t(0)


class _ConvertOperation(Operation, GenericModel, Generic[AssetHbdT]):
    __operation_name__ = "convert"

    from_: AccountName = Field(alias="from")
    request_id: Uint32t = DEFAULT_REQUEST_ID
    amount: AssetHbdT


class ConvertOperation(_ConvertOperation[AssetHbdHF26]):
    ...


class ConvertOperationLegacy(_ConvertOperation[AssetHbdLegacy]):
    ...
