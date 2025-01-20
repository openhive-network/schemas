from __future__ import annotations

from abc import ABC
import json
from schemas.fields.assets import AssetBase, AssetHbd, AssetHive, AssetVest
from typing import Any, Generic, TypeVar
from typing_extensions import get_args
import contextlib

import msgspec

from schemas.fields.assets.asset_info import AssetInfo

ResolvedFromT = TypeVar("ResolvedFromT")
ResolvedT = TypeVar("ResolvedT")

class Resolvable(ABC, Generic[ResolvedT, ResolvedFromT]):
    @staticmethod
    def resolve(incoming_cls: type, value: ResolvedFromT) -> ResolvedT:
        ...


StringResolvedT = TypeVar("StringResolvedT", bound=str)

def is_valid_json(string: str) -> bool:
    try:
        json.loads(string)
        return True
    except json.JSONDecodeError:
        return False

class OptionallyEmpty(str, Resolvable["OptionallyEmpty[StringResolvedT]", str], Generic[StringResolvedT]):
    @staticmethod
    def resolve(incoming_cls: type, value: str) -> "OptionallyEmpty[StringResolvedT]":
        if len(value) == 0:
            return OptionallyEmpty("")
        non_empty_str_t = get_args(incoming_cls)[0]
        if is_valid_json(value):
            return OptionallyEmpty(msgspec.json.decode(f'"{value}"', type=non_empty_str_t))
        else:
            return OptionallyEmpty(value)


AnyResolvedT = TypeVar("AnyResolvedT", bound=Any)
class JsonString(Resolvable["JsonString[AnyResolvedT]", Any], Generic[AnyResolvedT]):
    """
    It must be possible to get and set json content, load JsonString value form string and dump JsonString to string.
    JsonString has property value which allows to get and set json content as dict, list, str, int, float, bool or None.
    """

    @staticmethod
    def resolve(incoming_cls: type, value: str) -> "JsonString[AnyResolvedT]":
        if isinstance(value, str):
            try:
                return json.loads(value)
            except (ValueError, TypeError) as error:
                raise ValueError(f"Value is not a valid json string! Received `{value}`") from error
        if isinstance(value, (dict, list, tuple, str, int, float, bool, type(None))):
            return value
        raise ValueError(f"Value is not a valid type! Received `{value}` with type `{type(value)}`")


    # @classmethod
    # def validate(cls, value: Any) -> JsonString[JsonFieldType]:
    #     if isinstance(value, JsonString):
    #         value = value.value
    #         if isinstance(value, str):
    #             return cls.validate(f'"{value}"')
    #         return cls.validate(value)

    #     if isinstance(value, str):
    #         try:
    #             parsed = json.loads(value)
    #             return cls(parsed)
    #         except (ValueError, TypeError) as error:
    #             raise ValueError(f"Value is not a valid json string! Received `{value}`") from error
    #     if isinstance(value, get_args(AnyJson)):
    #         return cls(value)
    #     # if isinstance(value, PreconfiguredBaseModel):
    #     #     return cls(value)  # type: ignore[arg-type]

    #     raise ValueError(f"Value is not a valid type! Received `{value}` with type `{type(value)}`")

    # @property
    # def value(self) -> JsonFieldType:
    #     return self._value

    # @value.setter
    # def value(self, new_value: JsonFieldType) -> None:
    #     self._value = new_value

    # def serialize(self) -> str:
    #     """Dumps JsonString with no spaces between keys and values"""
    #     if isinstance(self._value, ApplicationOperation):
    #         return self._value.json()
    #     return json.dumps(self._value, separators=(",", ":"), ensure_ascii=False)

    # def __getitem__(self, key: str | int) -> AnyJson:
    #     self.__check_is_value_index_accessible()
    #     return self._value[key]  # type: ignore[index]

    # def __setitem__(self, key: str | int, value: AnyJson) -> None:
    #     self.__check_is_value_index_accessible()
    #     self._value[key] = value  # type: ignore[index]

    # def __check_is_value_index_accessible(self) -> None:
    #     if not isinstance(self._value, dict | list | tuple):
    #         raise TypeError(
    #             f"The value in JsonString must be dict, list or tuple use subscript, got: `{type(self._value)}`"
    #         )

    # def __eq__(self, other: object) -> bool:
    #     if isinstance(other, JsonString):
    #         return bool(self.value == other.value)
    #     return bool(self.value == other)


AssetResolved1T = TypeVar("AssetResolved1T", bound=AssetBase)
AssetResolved2T = TypeVar("AssetResolved2T", bound=AssetResolved1T)

def deduce_asset(potential_asset: str | dict[str, Any], asset_types: list[type[AssetBase]]) -> AssetBase:
    if isinstance(potential_asset, str):
        for asset in asset_types:
            with contextlib.suppress(ValueError): # suppress error during conversion
                return asset.from_legacy(potential_asset)
        raise ValueError("Cannot convert into any of given Asset types")

    assert isinstance(potential_asset, dict), f"Only dict and str is allowed in AssetUnion.resolve"
    for asset in asset_types:
        with contextlib.suppress(ValueError): # suppress error during conversion
            return asset.from_nai(potential_asset)
    raise ValueError("Cannot convert into any of given Asset types")

T = TypeVar("T", bound=type[AssetBase])
def create_hidden_asset(base: type[T], source_asset: AssetBase) -> T:
    class HiddenAssetType(base):
        @staticmethod
        def get_asset_information() -> AssetInfo:
            return source_asset.get_asset_information()
    return HiddenAssetType(amount=source_asset.amount, precision=source_asset.precision(), nai=source_asset.nai())

class AssetUnion(AssetBase, Resolvable["AssetUnion[AssetResolved1T, AssetResolved2T]", dict[str, Any] | str], Generic[AssetResolved1T, AssetResolved2T]):
    @staticmethod
    def resolve(incoming_cls: type, value: dict[str, Any] | str) -> "AssetUnion[AssetResolved1T, AssetResolved2T]":
        assets: tuple[type[AssetBase], type[AssetBase]] = get_args(incoming_cls)
        return create_hidden_asset(AssetUnion, deduce_asset(value, list(assets)))


class AnyAsset(AssetBase, Resolvable["AnyAsset", dict[str, Any] | str]):
    @staticmethod
    def resolve(incoming_cls: type, value: dict[str, Any] | str) -> "AnyAsset":
        return create_hidden_asset(AnyAsset, deduce_asset(value, [AssetHbd, AssetHive, AssetVest]))
