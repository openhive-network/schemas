"""function for adding keys/additional subschemas to main schemas"""

from schemas.__private.fundamental_schemas import Array, ArrayStrict, Map, Schema
from schemas.__private.custom_schemas import ApiOperationObject, Proposal
from .local_tools import get_schema


def add_schema_to_map(source: Schema, *, path: str = 'source', key: str, schema: Schema) -> None:
    schema_to_extend = get_schema(source, path)

    assert isinstance(schema_to_extend, (Map, ApiOperationObject, Proposal)), 'You are trying to add schema to object' \
                                                                              ' which is not a Map, ' \
                                                                              'ApiOperationObject or Proposal.'

    schema_to_extend[key] = schema


def add_schema_to_array(source: Schema, *, path: str = 'source', index=None, schema: Schema) -> None:
    schema_to_extend = get_schema(source, path)

    assert isinstance(schema_to_extend, (Array, ArrayStrict)), 'You are trying to add schema to object which is ' \
                                                               'not an Array or ArrayStrict'

    schema_to_extend.insert(index, schema)
