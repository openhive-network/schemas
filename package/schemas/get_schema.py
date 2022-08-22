from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


def get_schema(schema_name: str) -> Schema:
    api, method = schema_name.split('.')
    schemas_module = importlib.import_module(f'schemas.{api}.response_schemas')
    schema = getattr(schemas_module, method)
    try:
        return getattr(schemas_module, method)
    except:
        raise AttributeError(f'The "{method}" method in "{api}" API does not have a matching schema.'
                             f' This means that the schema does not exist.'
                             f' Add "{method}" schema definition to {schemas_module.__file__}')


def use_optional_schema(api_and_schemas):
    print()
    if isinstance(api_and_schemas, list):
        dict_order = [{'api': api[0], 'schema': api[1]} for api in api_and_schemas]
        for item in dict_order:
            if item['api'] == 'condenser_api':
                return item['schema']
    if isinstance(api_and_schemas, Schema):
        return api_and_schemas
    raise


# def select_this_one(request) -> bool:
#     # funkacja sprawdzająca czy dana schema powinna być walidowana
#     return isinstance(request.params['1'], int)
