from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


def get_schema(schema_name: str) -> type[PreconfiguredBaseModel]:
    def __snake_case_to_pascal_case(text: str) -> str:
        return "".join([segment.title() for segment in text.split("_")])

    api, method = schema_name.split(".")
    method = __snake_case_to_pascal_case(method)
    schemas_module = importlib.import_module(f"schemas.{api}.response_schemas")
    try:
        return getattr(schemas_module, method)  # type: ignore[no-any-return]
    except ImportError as e:
        raise AttributeError(
            f"""The "{method}" method in "{api}" API does not have a matching schema.
This means that the schema does not exist.
Add "{method}" schema definition to {schemas_module.__file__}"""
        ) from e
