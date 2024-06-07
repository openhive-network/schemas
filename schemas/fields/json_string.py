from __future__ import annotations

import json
from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator


class JsonString:
    """
    It must be possible to get and set json content, load JsonString value form string and dump JsonString to string.
    JsonString has property value which allows to get and set json content as dict, list, str, int, float, bool or None.
    """

    AnyJson: TypeAlias = dict[str, "AnyJson"] | list["AnyJson"] | str | int | float | bool | None

    def __init__(self, _value: AnyJson) -> None:
        self._value = _value

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate

    @classmethod
    def validate(cls, json_string: str | JsonString) -> JsonString:
        error_template = ValueError("The value could only be JsonString or string with valid json!")

        if isinstance(json_string, JsonString):
            return json_string

        if not isinstance(json_string, str):
            raise error_template

        try:
            parsed = json.loads(json_string)
        except (ValueError, TypeError) as error:
            raise error_template from error

        return cls(parsed)

    @property
    def value(self) -> AnyJson:
        return self._value

    @value.setter
    def value(self, new_value: AnyJson) -> None:
        self._value = new_value

    @property
    def as_string(self) -> str:
        """Dumps JsonString with no spaces between keys and values"""
        return json.dumps(self._value, separators=(",", ":"))
