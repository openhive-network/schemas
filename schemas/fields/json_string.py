from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, TypeAlias

from pydantic import BaseModel

if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator


AnyJson: TypeAlias = dict[str, "AnyJson"] | list["AnyJson"] | str | int | float | bool | None

class JsonString:
    """
    It must be possible to get and set json content, load JsonString value form string and dump JsonString to string.
    JsonString has property value which allows to get and set json content as dict, list, str, int, float, bool or None.
    """

    def __init__(self, value: AnyJson) -> None:
        self._value = value

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate

    @classmethod
    def validate(cls, json_: AnyJson | str | BaseModel | JsonString) -> JsonString:
        if isinstance(json_, JsonString):
            return json_

        if isinstance(json_, BaseModel):
            return cls(json_.dict())

        if isinstance(json_, str):
            try:
                return cls(json.loads(json_))
            except (ValueError, TypeError) as error:
                raise ValueError(f"Value is string and is not valid json! Received `{json_}`") from error

        return cls(json_)

    @property
    def value(self) -> AnyJson:
        return self._value

    @value.setter
    def value(self, new_value: AnyJson) -> None:
        self._value = new_value

    def serialize(self) -> str:
        """Dumps JsonString with no spaces between keys and values"""
        return json.dumps(self._value, separators=(",", ":"))

    def __getitem__(self, key: str) -> AnyJson:
        if not isinstance(self._value, dict):
            raise TypeError(f"The value in JsonString must be dict to use subscript, got: `{type(self._value)}`")
        return self._value[key]

    def __setitem__(self, key: str, value: AnyJson) -> None:
        if not isinstance(self._value, dict):
            raise TypeError(f"The value in JsonString must be dict to use subscript, got: `{type(self._value)}`")
        self._value[key] = value

    def __getattr__(self, key: str) -> Any:
        return getattr(self._value, key)
