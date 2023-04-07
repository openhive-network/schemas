from schemas.__private.fundamental_schemas import Array, ArrayStrict, Map, Schema
from schemas.__private.custom_schemas import ApiOperationObject, Proposal
from .local_tools import get_schema


def get_schema_to_reduce(source: Schema, path: str):
    # Remove last element from path, we don't want to get schema that will be deleted. We want to get box which holds
    # this element.
    try:
        path = path[:path.rindex('.')]
    except ValueError:
        path = 'source'
    schema_to_reduce = get_schema(source, path)
    return schema_to_reduce


def remove_schema_from_map(source: Schema, *, path: str = 'source'):
    key_to_delete = path.split('.')[-1]
    schema_to_reduce = get_schema_to_reduce(source, path)
    assert isinstance(schema_to_reduce, (Map, ApiOperationObject, Proposal)), 'You are trying to remove schema from' \
                                                                              ' object which is not a Map, ' \
                                                                              'ApiOperationObject or Proposal.'
    del schema_to_reduce[key_to_delete]


def remove_schema_from_array(source: Schema, *, path: str = 'source'):
    index_to_delete = int(path.split('.')[-1])
    schema_to_reduce = get_schema_to_reduce(source, path)
    assert isinstance(schema_to_reduce, (Array, ArrayStrict)), 'You are trying to remove schema from object which ' \
                                                               'is not an Array or ArrayStrict'

    del schema_to_reduce[index_to_delete]
