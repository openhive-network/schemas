"""
User-friendly field types - values checked only when created (`AccountName(".")` raises `FieldValidationError`).

- types of builtins (`AccountName` is a `str`, `Uint16t` an `int`, ...) are checked by msgspec by their forms of
  validation models (`schemas.fields.validation`) - the rules are defined once; `meta()` gives them
  (`Uint16t.meta().le`),
- integers of any size (`HiveInt`, `Int64t`, `Uint64t`) are plain `int`,
- assets (`Asset`), dates (`HiveDateTime`) and JSON embedded in strings (`JsonString`) are types of their own.

The types of builtins are not meant for msgspec models - hand-written models take the forms of
`schemas.fields.validation` (checked by msgspec itself); `HiveDateTime` and `JsonString` are decoded there by the hooks
(`schemas.decoders`).
"""

from __future__ import annotations

from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.json_string import JsonString
from schemas.fields.public import (
    HBD_ASSET,
    HIVE_ASSET,
    KNOWN_ASSETS,
    VESTS_ASSET,
    Asset,
    AssetFactory,
    AssetInfo,
    AssetKind,
    AssetNaiAmount,
    SatoshiFactory,
    TokensFactory,
    asset_info_of_nai,
    asset_info_of_symbol,
)

from ._fields import (
    AccountName,
    BlockId,
    CustomIdType,
    HardforkVersion,
    Hex,
    HiveInt,
    Identifier,
    Int16t,
    Int64t,
    NodeType,
    OptionallyEmptyAccountName,
    Permlink,
    PrivateKey,
    PublicKey,
    Revision,
    Sha256,
    Signature,
    TransactionId,
    Uint8t,
    Uint16t,
    Uint32t,
    Uint64t,
    Version,
    WitnessUrl,
)

__all__ = [
    "HBD_ASSET",
    "HIVE_ASSET",
    "KNOWN_ASSETS",
    "VESTS_ASSET",
    "AccountName",
    "Asset",
    "AssetFactory",
    "AssetInfo",
    "AssetKind",
    "AssetNaiAmount",
    "BlockId",
    "CustomIdType",
    "HardforkVersion",
    "Hex",
    "HiveDateTime",
    "HiveInt",
    "Identifier",
    "Int16t",
    "Int64t",
    "JsonString",
    "NodeType",
    "OptionallyEmptyAccountName",
    "Permlink",
    "PrivateKey",
    "PublicKey",
    "Revision",
    "SatoshiFactory",
    "Sha256",
    "Signature",
    "TokensFactory",
    "TransactionId",
    "Uint8t",
    "Uint16t",
    "Uint32t",
    "Uint64t",
    "Version",
    "WitnessUrl",
    "asset_info_of_nai",
    "asset_info_of_symbol",
]
