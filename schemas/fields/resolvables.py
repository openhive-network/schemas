from __future__ import annotations

from abc import ABC
import json
from schemas.fields.assets import AssetBase, AssetHbd, AssetHive, AssetVest
from typing import Any, Generic, TypeVar, cast
from typing_extensions import get_args
import contextlib

import msgspec

from schemas.fields.assets._base import AssetNaiAmount
from schemas.fields.assets.asset_info import AssetInfo
from schemas.fields.hive_int import HiveInt

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
    return HiddenAssetType(amount=source_asset.amount, precision=source_asset.precision, nai=source_asset.nai)

class AssetUnion(AssetBase, Resolvable["AssetUnion[AssetResolved1T, AssetResolved2T]", dict[str, Any] | str], Generic[AssetResolved1T, AssetResolved2T]):
    @staticmethod
    def resolve(incoming_cls: type, value: dict[str, Any] | str) -> "AssetUnion[AssetResolved1T, AssetResolved2T]":
        assets: tuple[type[AssetBase], type[AssetBase]] = get_args(incoming_cls)
        return create_hidden_asset(AssetUnion, deduce_asset(value, list(assets)))


class AnyAsset(AssetBase, Resolvable["AnyAsset", dict[str, Any] | str]):
    @staticmethod
    def resolve(incoming_cls: type, value: dict[str, Any] | str) -> "AnyAsset":
        return create_hidden_asset(AnyAsset, deduce_asset(value, [AssetHbd, AssetHive, AssetVest]))
