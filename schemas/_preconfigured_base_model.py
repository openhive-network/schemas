"""
Common configuration for all classes(except some hive_fields), here you can add config that all classes which
inheritance from this class must have
"""

from __future__ import annotations

import copy
from dataclasses import dataclass
from enum import IntEnum
from json import dumps as pretty_json_dumps
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast, get_args, get_origin

import msgspec
from typing_extensions import Self

from schemas.policies.extra_fields import ExtraFieldsPolicy

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator

    from schemas.decoders import DecoderFactory

DictStrAny = dict[str, Any]
DictStrAnyType = dict[str, type[Any]]


@dataclass
class MemberTypeName:
    full: str
    outer: str
    inners: list[str]


class SwapType(IntEnum):
    NONE = -1  # do nothing
    STANDARD = 0  # replace value as is
    ITERABLE = 1  # iterate over collection and replace all values


class PreconfiguredBaseModel(
    msgspec.Struct, omit_defaults=True, forbid_unknown_fields=not ExtraFieldsPolicy.is_allowed()
):
    def __post_init__(self) -> None:
        from schemas.policies.disable_swap_types import DisableSwapTypes

        if not DisableSwapTypes.is_disabled():
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

    def __contains__(self, key: str) -> bool:
        return key in self.dict()

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

    def dict(
        self,
        *,
        exclude: set[str] | None = None,
        exclude_none: bool = False,
        exclude_defaults: bool = False,
    ) -> DictStrAny:
        data: DictStrAny = {}
        defaults = (
            dict(zip(self.__struct_fields__, self.__struct_defaults__, strict=False))
            if hasattr(self, "__struct_defaults__")
            else {}
        )

        for key, value in dict(self).items():
            if exclude_none and value is None:
                continue

            if exclude_defaults and key in defaults and value == defaults[key]:
                continue

            if exclude is not None and key in exclude:
                continue

            data[key] = value

        return data

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        """Allow the object to be converted to a dictionary using dict()."""
        for key, item in msgspec.structs.asdict(self).items():
            yield (key.strip("_"), item)  # Strip underscores from keys to match dict() behavior

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

    def __slice_member_type_name(self, member_type_name: Any) -> MemberTypeName:
        """
        Returns encoded sliced typename.

        Args:
            member_type_name: Type name to be encoded and sliced.

        Returns:
            Tuple of encoded type name, inner type names and type name without brackets.

        Note:
            In case of non-generic types, the first element of the tuple will be the same as the third
            and second will be an empty list.
        """
        result = MemberTypeName(full="", outer="", inners=[])

        if not isinstance(member_type_name, str):
            result.full = str(member_type_name)
            if member_type_name is not type:
                result.outer = str(get_origin(member_type_name))
                result.inners = [str(x) for x in get_args(member_type_name)]
        else:
            result.full = member_type_name
        assert isinstance(result.full, str), "Invalid typename conversion"

        if (bracket_pos := result.full.find("[")) < 0:
            return result

        if len(result.inners) == 0:
            result.outer = result.full[:bracket_pos]
            result.inners = [item.strip() for item in result.full[bracket_pos + 1 : -1].split(",")]

        return result

    def __detect_swap_type(
        self,
        registered_types: DictStrAnyType,
        member_type_name: MemberTypeName,
        is_builtin: bool,
        is_iterable: bool,
    ) -> tuple[SwapType, type[Any] | None]:
        """
        Check if the type is convertible to the registered type.

        Args:
            member_type_name: Type name to be checked.

        Returns:
            True if the type is convertible, False otherwise.
        """

        if not is_builtin:
            return SwapType.NONE, None

        if (
            result := registered_types.get(member_type_name.full, registered_types.get(member_type_name.outer))
        ) is not None:
            return SwapType.STANDARD, result

        if is_iterable:
            assert len(member_type_name.inners) > 0, f"Invalid (untyped) typename: {member_type_name.full}"
            found_types = [x for x in [registered_types.get(tn) for tn in member_type_name.inners] if x is not None]
            if len(found_types) > 0:
                return SwapType.ITERABLE, found_types[0]

        return SwapType.NONE, None

    def __convert_to_target_value(self, current_value: Any, target_type: type[Any]) -> Any:
        from schemas.decoders import dec_hook_hf26

        return msgspec.convert(current_value, type=target_type, dec_hook=dec_hook_hf26)

    def __swap_to_registered_types(self) -> None:
        if not hasattr(self, "__annotations__"):
            return

        registered_types = self._registered_swap_types()
        assert registered_types is not None

        for member_name, member_type_name in cast(dict[str, str], self.__annotations__).items():
            typename = self.__slice_member_type_name(member_type_name)
            current_member_value = getattr(self, member_name)
            is_buildins = any(
                isinstance(current_member_value, builtin_type)
                for builtin_type in [int, str, bool, float, dict, tuple, list, set]
            )
            is_supported_iterable_buildins = (
                any(isinstance(current_member_value, builtin_type) for builtin_type in [list, set])
                and len(current_member_value) > 0
            )
            swap_type, target_type = self.__detect_swap_type(
                registered_types=registered_types,
                member_type_name=typename,
                is_builtin=is_buildins,
                is_iterable=is_supported_iterable_buildins,
            )

            if swap_type == SwapType.NONE or target_type is None:
                continue

            target_member_value = current_member_value
            if swap_type == SwapType.STANDARD:
                target_member_value = self.__convert_to_target_value(current_member_value, target_type)
            elif swap_type == SwapType.ITERABLE:
                target_member_value = type(current_member_value)(
                    [self.__convert_to_target_value(item, target_type) for item in current_member_value]
                )
            setattr(self, member_name, target_member_value)

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
    def _registered_swap_types(cls) -> DictStrAnyType:
        """Types registered by this method will be swapped to them from builtins during __post_init__.

        Note: Can be overrided by sub-classes to add more types.
        """
        from schemas.fields._init_validators import InitValidator
        from schemas.fields.hive_datetime import HiveDateTime
        from schemas.fields.resolvables import (
            AssetUnionAssetHiveAssetHbd,
            AssetUnionAssetHiveAssetVests,
            JsonString,
        )

        result = {
            "AssetUnionAssetHiveAssetHbd": AssetUnionAssetHiveAssetHbd,
            "AssetUnionAssetHiveAssetVests": AssetUnionAssetHiveAssetVests,
            "JsonString": JsonString[Any],
            "HiveDateTime": HiveDateTime,
        }
        result.update(InitValidator.get_registered_types())
        return result  # type: ignore[return-value]

    def __hash__(self) -> int:
        return hash(self.json())


BaseModelT = TypeVar("BaseModelT", bound=PreconfiguredBaseModel)
