from __future__ import annotations

from typing import Any, Generic, TypeVar

import msgspec

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.errors import FieldValidationError
from schemas.fields.serializable import Serializable

__all__ = [
    "JsonString",
]

AnyResolvedT = TypeVar("AnyResolvedT")


class JsonString(Serializable, Generic[AnyResolvedT]):
    """
    It must be possible to get and set json content, load JsonString value form string and dump JsonString to string.
    JsonString has property value which allows to get and set json content as dict, list, str, int, float, bool or None.
    """

    value: Any  # Any: JSON content of a shape known only to the user, accessed dynamically (`value["a"]["b"]`)

    def __init__(self, value: object) -> None:
        if isinstance(value, JsonString):
            self.value = value.value
        else:
            self.value = self._parse(value=value)

    @staticmethod
    def _parse(value: object) -> object:
        if value is None:
            raise FieldValidationError("Value must not be None for JsonString")
        if isinstance(value, str):
            if len(value) == 0:
                return ""
            try:
                parsed = msgspec.json.decode(value)
                if isinstance(parsed, str):
                    return value
                return parsed  # noqa: TRY300
            except msgspec.DecodeError as error:
                raise FieldValidationError(f"Value is not a valid json string! Received `{value}`") from error
        if isinstance(value, dict | list | tuple | str | int | float | bool):
            return value
        if isinstance(value, PreconfiguredBaseModel):
            return value
        raise FieldValidationError(f"Value is not a valid type! Received `{value}` with type `{type(value)}`")

    def __eq__(self, other: object) -> bool:
        if isinstance(other, JsonString):
            return bool(self.value == other.value)
        return bool(self.value == other)

    def serialize(self) -> str:
        """Dumps JsonString with no spaces between keys and values"""
        if isinstance(self.value, PreconfiguredBaseModel):
            return self.value.json(remove_whitespaces=True)
        if isinstance(self.value, str):
            return self.value
        if isinstance(self.value, dict | tuple | list | set | int | float):
            return msgspec.json.encode(self.value).decode()
        raise TypeError(f"Incorrect type to encode: {type(self)}")

    def __getitem__(self, key: str | int) -> Any:  # Any: as `value` - item of JSON content of unknown shape
        self.__check_is_value_index_accessible()
        return self.value[key]

    def __setitem__(self, key: str | int, value: object) -> None:
        self.__check_is_value_index_accessible()
        self.value[key] = value

    def __check_is_value_index_accessible(self) -> None:
        if not isinstance(self.value, dict | list | tuple):
            raise TypeError(
                f"The value in JsonString must be dict, list or tuple use subscript, got: `{type(self.value)}`"
            )
