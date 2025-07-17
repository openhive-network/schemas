from __future__ import annotations

from schemas.apis.api_client_generator._private.common.converters import snake_to_camel
from schemas.apis.api_client_generator._private.description_tools import get_last_part_of_ref


def get_type_from_ref_in_camel(ref: str) -> str:
    """Get type from OpenAPI $ref property and convert it to the CamelCase."""
    last_part = get_last_part_of_ref(ref)
    type_name = last_part.split(".")[-1] if "." in last_part else last_part

    return snake_to_camel(type_name)
