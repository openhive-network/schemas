from __future__ import annotations

import contextlib
import json
from abc import ABC
from typing import TYPE_CHECKING, Any, Generic, TypeVar, cast, get_args

import msgspec

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.assets import AssetBase, AssetHbd, AssetHive, AssetVests
from schemas.fields.assets.asset_info import AssetInfo
from schemas.fields.basic import AccountName, Permlink

ResolvedFromT = TypeVar("ResolvedFromT")
ResolvedT = TypeVar("ResolvedT")


class Resolvable(ABC, Generic[ResolvedT, ResolvedFromT]):
    @staticmethod
    def resolve(incoming_cls: type, value: ResolvedFromT) -> ResolvedT:  # type: ignore[empty-body]
        ...


StringResolvedT = TypeVar("StringResolvedT", bound=str)


class OptionallyEmpty(str, Resolvable["OptionallyEmpty[StringResolvedT]", str], Generic[StringResolvedT]):
    @staticmethod
    def resolve(incoming_cls: type, value: str) -> OptionallyEmpty[StringResolvedT]:
        if len(value) == 0:
            return OptionallyEmpty("")
        non_empty_str_t = get_args(incoming_cls)[0]
        return OptionallyEmpty(msgspec.convert(value, type=non_empty_str_t))

if TYPE_CHECKING:
    OptionallyEmptyAccountName = str
    OptionallyEmptyString = str
    OptionallyEmptyPermlink = str
else:
    OptionallyEmptyAccountName = OptionallyEmpty[AccountName]
    OptionallyEmptyString = OptionallyEmpty[str]
    OptionallyEmptyPermlink = OptionallyEmpty[Permlink]

AnyResolvedT = TypeVar("AnyResolvedT", bound=Any)


class JsonString(Resolvable["JsonString[AnyResolvedT]", Any], Generic[AnyResolvedT]):
    """
    It must be possible to get and set json content, load JsonString value form string and dump JsonString to string.
    JsonString has property value which allows to get and set json content as dict, list, str, int, float, bool or None.
    """

    value: Any

    def __init__(self, value: Any) -> None:
        if isinstance(value, JsonString):
            self.value = value.value
        else:
            self.value = value

    @staticmethod
    def resolve(incoming_cls: type, value: Any) -> JsonString[AnyResolvedT]:  # ruff: noqa: ARG004
        if isinstance(value, str):
            try:
                parsed = msgspec.json.decode(value)
                return JsonString(parsed)
            except (ValueError, TypeError) as error:
                raise ValueError(f"Value is not a valid json string! Received `{value}`") from error
        if isinstance(value, dict | list | tuple | str | int | float | bool | type(None)):
            return JsonString(value)
        if isinstance(value, PreconfiguredBaseModel):
            return JsonString(value)
        raise ValueError(f"Value is not a valid type! Received `{value}` with type `{type(value)}`")

    def __eq__(self, other: object) -> bool:
        if isinstance(other, JsonString):
            return bool(self.value == other.value)
        return bool(self.value == other)

    def serialize(self) -> str:
        """Dumps JsonString with no spaces between keys and values"""
        from schemas.application_operation import ApplicationOperation

        if isinstance(self.value, ApplicationOperation):
            return self.value.json(remove_whitespaces=True)
        if isinstance(self.value, dict):
            return json.dumps(self.value, separators=(",", ":"))
        if isinstance(self.value, list):
            return json.dumps(self.value, separators=(",", ":"))
        if isinstance(self.value, str):
            return self.value
        raise TypeError(f"Incorrect type to serialize: {type(self)}")

    def encode_json(self) -> str:
        """Dumps JsonString with no spaces between keys and values"""
        from schemas.application_operation import ApplicationOperation

        if isinstance(self.value, ApplicationOperation):
            return self.value.json(remove_whitespaces=True)
        if isinstance(self.value, dict):
            return json.dumps(self.value, separators=(",", ":"))
        if isinstance(self.value, str):
            return json.dumps(json.dumps(self.value))
        if isinstance(self.value, list):
            return json.dumps(self.value, separators=(",", ":"))
        if isinstance(self.value, float):
            return json.dumps(json.dumps(self.value))
        raise TypeError(f"Incorrect type to encode: {type(self)}")

    def encode(self) -> str:
        """Dumps JsonString with no spaces between keys and values"""
        from schemas.application_operation import ApplicationOperation

        if isinstance(self.value, ApplicationOperation):
            return self.value.json(remove_whitespaces=True)
        if isinstance(self.value, dict):
            return json.dumps(json.dumps(self.value))
        if isinstance(self.value, str):
            return json.dumps(json.dumps(self.value))
        if isinstance(self.value, list):
            return json.dumps(self.value, separators=(",", ":"))
        if isinstance(self.value, float):
            return json.dumps(json.dumps(self.value))
        raise TypeError(f"Incorrect type to encode: {type(self)}")

    def __getitem__(self, key: str | int) -> Any:
        self.__check_is_value_index_accessible()
        return self.value[key]

    def __setitem__(self, key: str | int, value: Any) -> None:
        self.__check_is_value_index_accessible()
        self.value[key] = value

    def __check_is_value_index_accessible(self) -> None:
        if not isinstance(self.value, dict | list | tuple):
            raise TypeError(
                f"The value in JsonString must be dict, list or tuple use subscript, got: `{type(self.value)}`"
            )


AssetResolved1T = TypeVar("AssetResolved1T", bound=AssetBase)
AssetResolved2T = TypeVar("AssetResolved2T", bound=AssetBase)


def deduce_asset(potential_asset: str | dict[str, Any], asset_types: list[type[AssetBase]]) -> AssetBase:
    if isinstance(potential_asset, str):
        for asset in asset_types:
            with contextlib.suppress(ValueError):  # suppress error during conversion
                return asset.from_legacy(potential_asset)
        raise ValueError("Cannot convert into any of given Asset types")

    assert isinstance(potential_asset, dict), "Only dict and str is allowed in AssetUnion.resolve"
    for asset in asset_types:
        with contextlib.suppress(ValueError):  # suppress error during conversion
            return asset.from_nai(potential_asset)
    raise ValueError("Cannot convert into any of given Asset types")


T = TypeVar("T", bound=type[AssetBase])


def create_hidden_asset(base: T, source_asset: AssetBase) -> T:
    class HiddenAssetType(base):  # type: ignore[valid-type, misc]
        @staticmethod
        def get_asset_information() -> AssetInfo:
            return source_asset.get_asset_information()

    return HiddenAssetType(amount=source_asset.amount, precision=source_asset.precision(), nai=source_asset.nai())


class AssetUnion(
    AssetBase,
    Resolvable["AssetUnion[AssetResolved1T, AssetResolved2T]", dict[str, Any] | str],
    Generic[AssetResolved1T, AssetResolved2T],
):
    @staticmethod
    def resolve(incoming_cls: type, value: dict[str, Any] | str) -> AssetUnion[AssetResolved1T, AssetResolved2T]:
        assets = cast(tuple[type[AssetBase], type[AssetBase]], get_args(incoming_cls))
        return cast(
            AssetUnion[AssetResolved1T, AssetResolved2T],
            create_hidden_asset(AssetUnion, deduce_asset(value, list(assets))),
        )


class AnyAsset(AssetBase, Resolvable["AnyAsset", dict[str, Any] | str]):
    @staticmethod
    def resolve(incoming_cls: type, value: dict[str, Any] | str) -> AnyAsset:  # ruff: noqa: ARG004
        return cast(AnyAsset, create_hidden_asset(AnyAsset, deduce_asset(value, [AssetHbd, AssetHive, AssetVests])))
