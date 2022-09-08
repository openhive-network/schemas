from typing import Any, Callable, Dict, List, Tuple

from schemas.__private.fundamental_schemas import Schema
from schemas.get_schema import Request


class SchemaSelector:
    def __init__(self, predicates_and_schemas: List[Tuple[Callable, Schema]]):
        self.__predicates_and_schemas = predicates_and_schemas

    def validate(self, instance: Dict[str, Any], request: Dict[str, Any]) -> None:
        for predicate, schema in self.__predicates_and_schemas:
            if predicate(Request(request)):
                schema.validate(instance)
                break
