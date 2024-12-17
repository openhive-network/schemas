from __future__ import annotations

from typing import TYPE_CHECKING, Any, Protocol, TypeVar, get_origin

import msgspec
from msgspec.json import Decoder

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.market_history_api.fundaments_of_responses import BucketSizes
from schemas.apis.wallet_bridge_api.response_schemas import _GetActiveWitnesseslist
from schemas.fields.assets._base import AssetHbd, AssetHive, AssetNaiAmount, AssetVests
from schemas.fields.basic import Permlink, PublicKey
from schemas.fields.hex import Sha256
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.fields.resolvables import AnyAsset, Resolvable
from schemas.fields.version import Version

if TYPE_CHECKING:
    from collections.abc import Callable


class DecoderFactory(Protocol):
    def __call__(self, cls: type[PreconfiguredBaseModel]) -> Decoder[type[PreconfiguredBaseModel]]:
        ...


def dec_hook_base(type_: type, obj: Any) -> Any:
    # Słownik mapujący typy do odpowiednich funkcji lub klas
    type_handlers: dict[type, Callable[[Any], Any]] = {
        HiveInt: HiveInt,
        HiveDateTime: HiveDateTime,
        BucketSizes: BucketSizes,
        AssetNaiAmount: AssetNaiAmount,
        Permlink: Permlink,
        PublicKey: PublicKey,
        Sha256: Sha256,
        Version: Version,
        # TransactionId: TransactionId,
        # Hex: Hex,
        # Url: Url,
        # CustomIdType: CustomIdType,
        _GetActiveWitnesseslist: _GetActiveWitnesseslist,
        AnyAsset: lambda obj: AnyAsset.resolve(type_, obj),  # Obsługuje AnyAsset specyficznie
    }

    # Sprawdzamy, czy typ znajduje się w słowniku
    handler = type_handlers.get(type_)
    if handler:
        return handler(obj)

    # Obsługa dla typów, które są subklasami Resolvable
    orig_type = get_origin(type_)
    if orig_type is not None and issubclass(orig_type, Resolvable):
        return type_.resolve(type_, obj)  # type: ignore

    # Jeśli typ nie jest obsługiwany, rzucamy wyjątek
    raise NotImplementedError(f"Objects of type {type_} are not supported")


def dec_hook_legacy(type_: type, obj: Any) -> Any:
    if type_ is AssetVests:
        return AssetVests.from_legacy(obj)
    if type_ is AssetHive:
        return AssetHive.from_legacy(obj)
    if type_ is AssetHbd:
        return AssetHbd.from_legacy(obj)
    return dec_hook_base(type_, obj)


def dec_hook_hf26(type_: type, obj: Any) -> Any:
    if type_ is AssetVests:
        return AssetVests.from_nai(obj)
    if type_ is AssetHive:
        return AssetHive.from_nai(obj)
    if type_ is AssetHbd:
        return AssetHbd.from_nai(obj)
    return dec_hook_base(type_, obj)


T = TypeVar("T")


def get_legacy_decoder(type_: type[T]) -> Decoder[T]:
    return msgspec.json.Decoder(type_, dec_hook=dec_hook_legacy)


def get_hf26_decoder(type_: type[T]) -> Decoder[T]:
    return msgspec.json.Decoder(type_, dec_hook=dec_hook_hf26)
