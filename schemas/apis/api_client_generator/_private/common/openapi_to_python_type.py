from __future__ import annotations

OPENAPI_BASIC_TYPES_MAPPING: dict[str, type] = {
    "string": str,
    "integer": int,
    "number": float,
    "boolean": bool,
    "array": list,
    "object": dict,
}


def convert_openapi_type_to_python_type(openapi_type: str) -> type:
    """
    Convert OpenAPI type to Python type.

    Args:
        openapi_type: The OpenAPI type to convert.

    Returns:
        The corresponding Python type.

    Raises:
        ValueError: If the OpenAPI type is not supported.
    """

    if openapi_type not in OPENAPI_BASIC_TYPES_MAPPING:
        raise ValueError(
            f"Unsupported OpenAPI type: {openapi_type}. Supported types are: {', '.join(OPENAPI_BASIC_TYPES_MAPPING.keys())}."
        )

    return OPENAPI_BASIC_TYPES_MAPPING[openapi_type]
