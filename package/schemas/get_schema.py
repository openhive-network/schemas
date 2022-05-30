from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema


def get_schema(schema_name: str) -> Schema:
    api, method = schema_name.split('.')
    schemas_module = importlib.import_module(f'schemas.{api}.response_schemas')
    try:
        return getattr(schemas_module, method)
    except:
        raise AttributeError(f'The "{method}" method in "{api}" API does not have a matching schema.'
                             f' This means that the schema does not exist.'
                             f' Add "{method}" schema definition to {schemas_module.__file__}')
