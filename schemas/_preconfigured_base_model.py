"""
    Common configuration for all classes(except some hive_fields), here you can add config that all classes which
    inheritance from this class must have
"""

from __future__ import annotations

import types
import typing
from datetime import datetime
from typing import Any, TypeVar, get_args, get_origin

import pydantic
from pydantic import BaseModel, Extra, Field, create_model  # pyright: ignore
from typing_extensions import Self

from schemas.hive_constants import HIVE_TIME_FORMAT


class PreconfiguredBaseModel(BaseModel):
    class Config:
        extra = Extra.forbid
        allow_population_by_field_name = True
        smart_union = True
        json_encoders = {datetime: lambda x: x.strftime(HIVE_TIME_FORMAT)}  # noqa: RUF012

    @classmethod
    def __is_aliased_field_name(cls, field_name: str) -> bool:
        return field_name in {
            "id",
            "from",
            "json",
            "schema",
            "open",
            "field",
            "input",
            "hex",
        }

    def __getitem__(self, key: str) -> Any:
        """
        This allows using any schema from this repo as dictionary
        """
        key = self.__get_field_name(key)
        return getattr(self, key)

    def __setitem__(self, key: str, value: Any) -> None:
        """
        This allows using any schema from this repo as dictionary
        """
        key = self.__get_field_name(key)
        setattr(self, key, value)

    def shallow_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in self.__dict__.items():
            result[key.strip("_")] = value
        return result

    @classmethod
    def as_strict_model(cls, recursively: bool = True) -> type[Self]:  # noqa: C901
        """
        Generate a BaseModel class with all the same fields like the class on which the method was called but with
        required fields only (no defaults allowed).

        Returns:
            Strict version of the class
        """

        # ellipsis is used to indicate that the field is required
        field_definitions = {field.name: (field.type_, Field(alias=field.alias)) for field in cls.__fields__.values()}

        def process_type(type_: Any) -> Any:  # noqa: PLR0911
            def resolve_for_all_args(outer_type: Any) -> Any:
                return outer_type[tuple(process_type(arg) for arg in get_args(type_))]

            type_origin = get_origin(type_)
            if (
                type_ in {type(None), typing.Any}
                or type(type_) in {typing.TypeVar, pydantic.fields.FieldInfo}
                or type_origin in {typing.Literal}
            ):
                return type_

            if type_origin is not None:
                if type_origin in {types.UnionType, typing.Union}:
                    return resolve_for_all_args(typing.Union)

                if type_origin in {tuple, typing.Tuple}:  # noqa: UP006
                    return resolve_for_all_args(typing.Tuple)  # noqa: UP006

                if type_origin in {list, typing.List}:  # noqa: UP006
                    return resolve_for_all_args(typing.List)  # noqa: UP006

                if type_origin in {typing.Annotated}:
                    return resolve_for_all_args(typing.Annotated)

            if issubclass(type_, PreconfiguredBaseModel):
                return type_.as_strict_model()
            return type_

        if recursively:
            for field_name, pack in field_definitions.items():
                field_definitions[field_name] = (process_type(pack[0]), ...)

        return create_model(f"{cls.__name__}Strict", **field_definitions, __base__=PreconfiguredBaseModel)  # type: ignore

    def __get_field_name(self, name: str) -> str:
        if not hasattr(self, name) and self.__is_aliased_field_name(name):
            name = f"{name}_"

        assert hasattr(
            self, name
        ), f"`{name}` does not exists in `{self.__class__.__name__}`, available are: {list(self.dict().keys())}"
        return name


BaseModelT = TypeVar("BaseModelT", bound=PreconfiguredBaseModel)
