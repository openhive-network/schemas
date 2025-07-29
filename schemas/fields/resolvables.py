from __future__ import annotations

import contextlib
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Generic, Self, TypeGuard, TypeVar, cast, get_args, get_origin

import msgspec

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.assets import AssetBase, AssetHbd, AssetHive, AssetVests
from schemas.fields.assets._base import HiddenAssetBase
from schemas.fields.assets.asset_info import AssetInfo
from schemas.fields.hive_int import HiveInt
from schemas.fields.serializable import Serializable

ResolvedFromT = TypeVar("ResolvedFromT")
ResolvedT = TypeVar("ResolvedT")


class Resolvable(Serializable, Generic[ResolvedT, ResolvedFromT], ABC):
    @staticmethod
    @abstractmethod
    def resolve(incoming_cls: type, value: ResolvedFromT) -> ResolvedT:
        """
        Resolve the value to the type specified by incoming_cls.
        This method should be implemented by subclasses to provide specific resolution logic.
        """

    @staticmethod
    def is_resolvable(cls_: type[Any] | Any) -> TypeGuard[Resolvable[Any, Any]]:
        with contextlib.suppress(TypeError):  # try to handle easiest case first
            return issubclass(cls_, Resolvable)

        if cls_ is not type and get_origin(cls_) is None:
            cls_ = type(cls_)
        orig_type = get_origin(cls_)
        if orig_type is None:
            return issubclass(cls_, Resolvable)
        return issubclass(orig_type, Resolvable)


StringResolvedT = TypeVar("StringResolvedT", bound=str)


class OptionallyEmpty(str, Resolvable["OptionallyEmpty[StringResolvedT]", str], Generic[StringResolvedT]):
    @staticmethod
    def resolve(incoming_cls: type, value: str) -> OptionallyEmpty[StringResolvedT]:
        if len(value) == 0:
            return OptionallyEmpty("")
        non_empty_str_t = get_args(incoming_cls)[0]
        return OptionallyEmpty(msgspec.convert(value, type=non_empty_str_t))

    def serialize(self) -> Self:
        return self


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
    def resolve(incoming_cls: type, value: Any) -> JsonString[AnyResolvedT]:  # noqa: ARG004
        assert value is not None, "Value must not be None for JsonString.resolve"
        if isinstance(value, str):
            if len(value) == 0:
                return JsonString("")
            try:
                parsed = msgspec.json.decode(value)
                if isinstance(parsed, str):
                    return JsonString(value)
                return JsonString(parsed)
            except (ValueError, TypeError) as error:
                raise ValueError(f"Value is not a valid json string! Received `{value}`") from error
        if isinstance(value, dict | list | tuple | str | int | float | bool):
            return JsonString(value)
        if isinstance(value, PreconfiguredBaseModel):
            return JsonString(value)
        raise ValueError(f"Value is not a valid type! Received `{value}` with type `{type(value)}`")

    def __eq__(self, other: object) -> bool:
        if isinstance(other, JsonString):
            return bool(self.value == other.value)
        return bool(self.value == other)

    def encode_json(self) -> str:
        return self.serialize()

    def serialize(self) -> str:
        """Dumps JsonString with no spaces between keys and values"""
        from schemas.application_operation import ApplicationOperation

        if isinstance(self.value, ApplicationOperation):
            return self.value.json(remove_whitespaces=True)
        if isinstance(self.value, str):
            return self.value
        if isinstance(self.value, dict | tuple | list | set | int | float):
            return msgspec.json.encode(self.value).decode()
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


def deduce_asset(potential_asset: str | dict[str, Any] | AssetBase, asset_types: list[type[AssetBase]]) -> AssetBase:
    if isinstance(potential_asset, AssetBase):
        if type(potential_asset) in asset_types:
            return potential_asset
        raise ValueError(
            f"Given asset is not one of required: given: {potential_asset.as_nai()}, required: {asset_types}"
        )

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

        @classmethod
        def allowed_types(cls) -> list[type[AssetBase]]:
            return [type(source_asset)]

    return HiddenAssetType(amount=source_asset.amount, precision=source_asset.precision(), nai=source_asset.nai())


class AssetUnion(
    HiddenAssetBase,
    Resolvable["AssetUnion[AssetResolved1T, AssetResolved2T]", dict[str, Any] | str],
    Generic[AssetResolved1T, AssetResolved2T],
):
    @staticmethod
    def resolve(incoming_cls: type, value: dict[str, Any] | str) -> AssetUnion[AssetResolved1T, AssetResolved2T]:
        assert issubclass(incoming_cls, HiddenAssetBase), "Incoming class must be a HiddenAssetBase subclass"
        return cast(
            AssetUnion[AssetResolved1T, AssetResolved2T],
            create_hidden_asset(AssetUnion, deduce_asset(value, incoming_cls.allowed_types())),
        )

    def serialize(self) -> dict[str, str | HiveInt]:
        return self.as_serialized_nai()

    def serialize_as_legacy(self) -> Any:
        return self.as_legacy()

    @classmethod
    def factory(cls, name: str, allowed_assets: list[type[AssetBase]]) -> type[AssetUnion[AssetBase, AssetBase]]:
        class FactoryAssetUnion(AssetUnion[AssetBase, AssetBase]):
            __name__ = name

            @classmethod
            def allowed_types(cls) -> list[type[AssetBase]]:
                return allowed_assets

        return FactoryAssetUnion


class AnyAssetImpl(HiddenAssetBase, Resolvable["AnyAssetImpl", dict[str, Any] | str]):
    @staticmethod
    def resolve(incoming_cls: type, value: dict[str, Any] | str) -> AnyAssetImpl:  # noqa: ARG004
        return cast(
            AnyAssetImpl, create_hidden_asset(AnyAssetImpl, deduce_asset(value, [AssetHbd, AssetHive, AssetVests]))
        )

    def serialize(self) -> dict[str, str | HiveInt]:
        return self.as_serialized_nai()

    def serialize_as_legacy(self) -> Any:
        return self.as_legacy()

    @classmethod
    def allowed_types(cls) -> list[type[AssetBase]]:
        return [AssetHbd, AssetHive, AssetVests]


if TYPE_CHECKING:
    AssetUnionAssetHiveAssetHbd = AssetHive | AssetHbd
    AssetUnionAssetHiveAssetVests = AssetHive | AssetVests
    AnyAsset = AssetHive | AssetHbd | AssetVests
else:
    AssetUnionAssetHiveAssetHbd = AssetUnion.factory("AssetUnionAssetHiveAssetHbd", [AssetHive, AssetHbd])
    AssetUnionAssetHiveAssetVests = AssetUnion.factory("AssetUnionAssetHiveAssetVests", [AssetHive, AssetVests])
    AnyAsset = AnyAssetImpl
