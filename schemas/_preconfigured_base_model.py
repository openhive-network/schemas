"""
    Common configuration for all classes(except some hive_fields), here you can add config that all classes which
    inheritance from this class must have
"""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Literal, TypeVar

import msgspec

if TYPE_CHECKING:
    from collections.abc import Iterable

DictStrAny = dict[str, Any]


class PreconfiguredBaseModel(msgspec.Struct):
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

    def json(
        self,
        *,
        str_keys: bool = False,
        builtin_types: Iterable[type] | None = None,
        order: Literal[None, "deterministic", "sorted"] = None,
    ) -> str:
        from schemas.encoders import enc_hook_hf26

        return json.dumps(
            msgspec.to_builtins(
                obj=self, enc_hook=enc_hook_hf26, str_keys=str_keys, builtin_types=builtin_types, order=order
            )
        )

    def shallow_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in self.__dict__.items():
            if value is not None:
                result[key.strip("_")] = value
        return result

    def dict(  # noqa: A003
        self,
        *,
        exclude_none: bool = False,
        exclude_defaults: bool = False,
    ) -> DictStrAny:
        data = msgspec.structs.asdict(self)

        if exclude_none:
            data = {key: value for key, value in data.items() if value is not None}

        if exclude_defaults and hasattr(self, "__struct_defaults__"):
            defaults = dict(zip(self.__struct_fields__, self.__struct_defaults__, strict=False))
            data = {key: value for key, value in data.items() if key in defaults and value != defaults[key]}

        return data

    def __get_field_name(self, name: str) -> str:
        if not hasattr(self, name) and self.__is_aliased_field_name(name):
            name = f"{name}_"

        assert hasattr(
            self, name
        ), f"`{name}` does not exists in `{self.__class__.__name__}`, available are: {list(self.dict().keys())}"
        return name


BaseModelT = TypeVar("BaseModelT", bound=PreconfiguredBaseModel)
