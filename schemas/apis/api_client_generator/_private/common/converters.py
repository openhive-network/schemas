from __future__ import annotations

import re


def snake_to_camel(name: str) -> str:
    """Converts a snake_case string to CamelCase."""
    return "".join(word.capitalize() for word in name.split("_"))


def camel_to_snake(name: str) -> str:
    """Converts a CamelCase string to snake_case."""
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()
