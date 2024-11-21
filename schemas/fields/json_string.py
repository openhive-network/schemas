from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Generic, TypeAlias, TypeVar, get_args

from schemas.application_operation import ApplicationOperation
from schemas.fields.serializable import Serializable

if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator


if TYPE_CHECKING:
    AnyJson: TypeAlias = (
        dict[str, "AnyJson"] | list["AnyJson"] | tuple["AnyJson", ...] | str | int | float | bool | None
    )
else:
    AnyJson: TypeAlias = dict | list | tuple | str | int | float | bool | None

JsonFieldType = TypeVar("JsonFieldType", bound=AnyJson | ApplicationOperation)


class JsonString(Serializable, Generic[JsonFieldType]):
    """
    It must be possible to get and set json content, load JsonString value form string and dump JsonString to string.
    JsonString has property value which allows to get and set json content as dict, list, str, int, float, bool or None.
    """

    def __init__(self, value: JsonFieldType) -> None:
        self._value: JsonFieldType = value

    @classmethod
    # TODO[pydantic]: We couldn't refactor `__get_validators__`, please create the `__get_pydantic_core_schema__` manually.
    # Check https://docs.pydantic.dev/latest/migration/#defining-custom-types for more information.
    def __get_validators__(cls) -> CallableGenerator:
        yield cls.validate

    @classmethod
    def validate(cls, value: Any) -> JsonString[JsonFieldType]:
        if isinstance(value, JsonString):
            value = value.value
            if isinstance(value, str):
                return cls.validate(f'"{value}"')
            return cls.validate(value)

        if isinstance(value, str):
            try:
                parsed = json.loads(value)
                return cls(parsed)
            except (ValueError, TypeError) as error:
                raise ValueError(f"Value is not a valid json string! Received `{value}`") from error
        if isinstance(value, get_args(AnyJson)):
            return cls(value)
        if isinstance(value, ApplicationOperation):
            return cls(value)  # type: ignore[arg-type]

        raise ValueError(f"Value is not a valid type! Received `{value}` with type `{type(value)}`")

    @property
    def value(self) -> JsonFieldType:
        return self._value

    @value.setter
    def value(self, new_value: JsonFieldType) -> None:
        self._value = new_value

    def serialize(self) -> str:
        """Dumps JsonString with no spaces between keys and values"""
        if isinstance(self._value, ApplicationOperation):
            return self._value.json()
        return json.dumps(self._value, separators=(",", ":"), ensure_ascii=False)

    def __getitem__(self, key: str | int) -> AnyJson:
        self.__check_is_value_index_accessible()
        return self._value[key]  # type: ignore[index]

    def __setitem__(self, key: str | int, value: AnyJson) -> None:
        self.__check_is_value_index_accessible()
        self._value[key] = value  # type: ignore[index]

    def __check_is_value_index_accessible(self) -> None:
        if not isinstance(self._value, dict | list | tuple):
            raise TypeError(
                f"The value in JsonString must be dict, list or tuple use subscript, got: `{type(self._value)}`"
            )

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, JsonString):
            return bool(self.value == other.value)
        return bool(self.value == other)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}[{self.value.__class__.__name__}]({self.value=})"
