from __future__ import annotations

import importlib
from typing import Any, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from schemas.__private.fundamental_schemas import Schema

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


class Request:
    def __init__(self, message: Dict[str, Any]):
        api_name, method_name = message['method'].split('.')
        self.api_name: str = api_name
        self.method_name: str = method_name
        self.params = message['params']
