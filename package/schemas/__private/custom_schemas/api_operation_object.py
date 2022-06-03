from __future__ import annotations

from typing import TYPE_CHECKING, Any

from schemas.__private.custom_schemas.custom_schema import CustomSchema
from schemas.__private.custom_schemas.transaction_id import TransactionId
from schemas.__private.fundamental_schemas import AnyOf, ArrayStrict, Bool, Date, Int, Map, Str

if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


class ApiOperationObject(CustomSchema):
    def __init__(self, **options: Any):
        super().__init__(**options)
        self.__data = Map({
            'trx_id': TransactionId(),
            'block': Int(),
            'trx_in_block': Int(),
            'op_in_trx': Int(),
            'virtual_op': Bool(),
            'operation_id': Int(),
            'timestamp': Date(),
            'op': AnyOf(
                Map({
                    'type': Str(),
                    'value': Map({}, allow_additional_properties=True),
                }),
                ArrayStrict(Str(), Map({}, allow_additional_properties=True))
            )
        })

    def __setitem__(self, key, schema):
        self.__data[key] = schema

    def __delitem__(self, key):
        del self.__data[key]

    def _define_schema(self) -> Schema:
        return self.__data
