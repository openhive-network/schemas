"""
    Common configuration for all classes(except some hive_fields), here you can add config that all classes which
    inheritance from this class must have
"""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal, TypeVar, Callable, cast

import msgspec

if TYPE_CHECKING:
    from collections.abc import Iterable

    from schemas.decoders import T

DictStrAny = dict[str, Any]


class PreconfiguredBaseModel(msgspec.Struct, omit_defaults=True):

    def __post_init__(self):
        self.__swap_to_registered_types()

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

    def json(  # noqa: PLR0913
        self,
        *,
        str_keys: bool = False,
        builtin_types: Iterable[type] | None = None,
        order: Literal[None, "deterministic", "sorted"] = None,
        exclude_none: bool = False,
        remove_whitespaces: bool = False,
    ) -> str:
        from schemas.encoders import enc_hook_hf26_json

        data = msgspec.to_builtins(
            obj=self, enc_hook=enc_hook_hf26_json, str_keys=str_keys, builtin_types=builtin_types, order=order
        )
        if exclude_none:
            data = {key: value for key, value in data.items() if value is not None}
        if remove_whitespaces:
            return json.dumps(data, separators=(",", ":"))
        return json.dumps(data)

    def shallow_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in self.dict().items():
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

    def __swap_to_registered_types(self) -> None:
        from schemas.decoders import dec_hook_hf26

        registered_types = self._registered_swap_types()
        for member_name, member_type_name in cast(dict[str, str], self.__annotations__).items():
            member_type_name_without_brackets = member_type_name.split("[")[0]
            current_member_value = getattr(self, member_name)
            is_buildins = any(current_member_value is builtin_type for builtin_type in [int, str, bool, float, list, dict, set, tuple])
            if is_buildins and (type_to_convert_to := registered_types.get(member_type_name, registered_types.get(member_type_name_without_brackets))) is not None:
                new_member_value = msgspec.convert(current_member_value, type=type_to_convert_to, dec_hook=dec_hook_hf26)
                setattr(self, member_name, new_member_value)


    @classmethod
    def parse_file(cls, path: Path, decoder_factory: Callable[[type[T]], msgspec.json.Decoder[T]]) -> type[PreconfiguredBaseModel]:
        with Path.open(path, encoding="utf-8") as file:
            raw = file.read()
            return cls.parse_raw(raw, decoder_factory)

    @classmethod
    def parse_raw(cls, raw: str, decoder_factory: Callable[[type[T]], msgspec.json.Decoder[T]]) -> type[PreconfiguredBaseModel]:
        decoder = decoder_factory(cls)
        return decoder.decode(raw)

    @classmethod
    def _registered_swap_types(cls) -> dict[str, type]:
        """Types registered by this method will be swapped to them from builtins during __post_init__.

        Note: Can be overrided by sub-classes to add more types.
        """
        from schemas.fields.resolvables import (
            OptionallyEmptyAccountName,
            OptionallyEmptyPermlink,
            OptionallyEmptyString,
            AssetUnionAssetHiveAssetHbd,
            AssetUnionAssetHiveAssetVests
        )

        return {
            "OptionallyEmptyAccountName": OptionallyEmptyAccountName,
            "OptionallyEmptyPermlink": OptionallyEmptyPermlink,
            "OptionallyEmptyString": OptionallyEmptyString,
            "AssetUnionAssetHiveAssetHbd": AssetUnionAssetHiveAssetHbd,
            "AssetUnionAssetHiveAssetVests": AssetUnionAssetHiveAssetVests
        }


BaseModelT = TypeVar("BaseModelT", bound=PreconfiguredBaseModel)
