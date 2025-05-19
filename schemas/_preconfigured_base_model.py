"""
    Common configuration for all classes(except some hive_fields), here you can add config that all classes which
    inheritance from this class must have
"""

from __future__ import annotations

import copy
from json import dumps as pretty_json_dumps
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

import msgspec
from typing_extensions import Self

if TYPE_CHECKING:
    from collections.abc import Iterable

    from schemas.decoders import DecoderFactory

DictStrAny = dict[str, Any]


class PreconfiguredBaseModel(msgspec.Struct, omit_defaults=True):
    def __post_init__(self) -> None:
        self.__swap_to_registered_types()

    @classmethod
    def __is_aliased_field_name(cls, field_name: str) -> bool:
        return field_name in {"id", "from", "json", "schema", "open", "field", "input", "hex", "type"}

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

    def __get_field_name(self, name: str) -> str:
        if not hasattr(self, name) and self.__is_aliased_field_name(name):
            name = f"{name}_"

        assert hasattr(
            self, name
        ), f"`{name}` does not exists in `{self.__class__.__name__}`, available are: {list(self.dict().keys())}"
        return name

    def json(  # noqa: PLR0913
        self,
        *,
        str_keys: bool = False,
        builtin_types: Iterable[type] | None = None,
        order: Literal[None, "deterministic", "sorted"] = None,
        exclude_none: bool = False,
        remove_whitespaces: bool = False,
        exclude: set[str] | None = None,
    ) -> str:
        data = self.__as_builtins(
            str_keys=str_keys, builtin_types=builtin_types, order=order, exclude_none=exclude_none, exclude=exclude
        )

        if remove_whitespaces:
            return msgspec.json.encode(data, order=order).decode()
        return pretty_json_dumps(data, sort_keys=(order == "sorted"), ensure_ascii=False)

    def shallow_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in self.dict().items():
            if value is not None:
                result[key.strip("_")] = getattr(self, key)
        return result

    def dict(
        self,
        *,
        exclude: set[str] | None = None,
        exclude_none: bool = False,
        exclude_defaults: bool = False,
    ) -> DictStrAny:
        data: DictStrAny = msgspec.structs.asdict(self)

        if exclude_none:
            data = {key: value for key, value in data.items() if value is not None}

        if exclude_defaults and hasattr(self, "__struct_defaults__"):
            defaults = dict(zip(self.__struct_fields__, self.__struct_defaults__, strict=False))
            data = {key: value for key, value in data.items() if key in defaults and value != defaults[key]}

        if exclude is not None:
            return {k: v for k, v in data.items() if k not in exclude}
        return data

    def __as_builtins(
        self,
        str_keys: bool = False,
        builtin_types: Iterable[type] | None = None,
        order: Literal[None, "deterministic", "sorted"] = None,
        exclude_none: bool = False,
        exclude: set[str] | None = None,
    ) -> DictStrAny:
        from schemas.encoders import enc_hook_hf26

        data: DictStrAny = msgspec.to_builtins(
            obj=self._get_object_for_serialization(),
            enc_hook=enc_hook_hf26,
            str_keys=str_keys,
            builtin_types=builtin_types,
            order=order,
        )
        if exclude_none:
            data = {key: value for key, value in data.items() if value is not None}

        if exclude is not None:
            return {k: v for k, v in data.items() if k not in exclude}
        return data

    def _get_object_for_serialization(self) -> Self:
        return self

    def __swap_to_registered_types(self) -> None:
        if not hasattr(self, "__annotations__"):
            return
        from schemas.decoders import dec_hook_hf26

        registered_types = self._registered_swap_types()
        for member_name, member_type_name in cast(dict[str, str], self.__annotations__).items():
            try:
                member_type_name_str = member_type_name.__name__ if member_type_name is not str else member_type_name  # type: ignore[attr-defined, comparison-overlap]
            except AttributeError:
                member_type_name_str = str(member_type_name)
            member_type_name_without_brackets = member_type_name_str.split("[")[0]
            current_member_value = getattr(self, member_name)
            is_buildins = any(
                isinstance(current_member_value, builtin_type)
                for builtin_type in [int, str, bool, float, list, dict, set, tuple]
            )
            assert registered_types is not None
            if (
                is_buildins
                and (
                    type_to_convert_to := registered_types.get(
                        member_type_name_str, registered_types.get(member_type_name_without_brackets)
                    )
                )
                is not None
            ):
                new_member_value = msgspec.convert(
                    current_member_value, type=type_to_convert_to, dec_hook=dec_hook_hf26
                )
                setattr(self, member_name, new_member_value)

    @classmethod
    def parse_file(cls, path: Path, custom_decoder_factory: DecoderFactory | None = None) -> Self:
        # Default decoder is hf26_decoder
        if custom_decoder_factory is None:
            from schemas.decoders import get_hf26_decoder

            custom_decoder_factory = get_hf26_decoder
        with Path.open(path, encoding="utf-8") as file:
            raw = file.read()
            return cls.parse_raw(raw, custom_decoder_factory)

    @classmethod
    def parse_raw(cls, raw: str, custom_decoder_factory: DecoderFactory | None = None) -> Self:
        # Default decoder is hf26_decoder
        if custom_decoder_factory is None:
            from schemas.decoders import get_hf26_decoder

            custom_decoder_factory = get_hf26_decoder
        decoder = custom_decoder_factory(cls)
        return cast(Self, decoder.decode(raw))

    @classmethod
    def parse_builtins(cls, raw: Any) -> Self:
        from schemas.decoders import dec_hook_hf26

        return msgspec.convert(obj=raw, type=cls, dec_hook=dec_hook_hf26)

    def copy(self, exclude: set[str] | None = None) -> Self:
        copied = copy.deepcopy(self)
        if exclude is not None:
            for to_exclude in exclude:
                setattr(copied, to_exclude, None)
        return copied

    @classmethod
    def schema_json(cls) -> str:
        from schemas.decoders import schema_hook

        schema = msgspec.json.schema(cls, schema_hook=schema_hook)
        return msgspec.json.encode(schema).decode()

    @classmethod
    def _registered_swap_types(cls) -> dict[str, type[Any]]:  # type: ignore[valid-type]
        """Types registered by this method will be swapped to them from builtins during __post_init__.

        Note: Can be overrided by sub-classes to add more types.
        """
        from schemas.fields._init_validators import InitValidator
        from schemas.fields.resolvables import (
            AssetUnionAssetHiveAssetHbd,
            AssetUnionAssetHiveAssetVests,
        )

        result = {
            "AssetUnionAssetHiveAssetHbd": AssetUnionAssetHiveAssetHbd,
            "AssetUnionAssetHiveAssetVests": AssetUnionAssetHiveAssetVests,
        }
        result.update(InitValidator.get_registered_types())  # type: ignore[arg-type]
        return result

    def __hash__(self) -> int:
        return hash(self.json())


BaseModelT = TypeVar("BaseModelT", bound=PreconfiguredBaseModel)
