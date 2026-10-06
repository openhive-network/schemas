"""
Builtin counterparts of the validating field types.

Every alias below is named exactly like the validating type it stands for, but resolves to plain python types
(the form in which the value appears in raw JSON). Generated public API models use these aliases, so they carry
the semantic name without importing any validation machinery.

`BASE_TYPE_MAPPINGS` maps each alias name to the dotted import path of its validating counterpart, which is used
by generated validation models. Values are strings on purpose - this module must stay import-light (no msgspec,
no other schemas modules).
"""

# ruff: noqa: UP040
# Aliases intentionally use `TypeAlias` (not the `type` statement) - at runtime they must be the plain types,
# so generated models resolve them to builtins.
from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

__all__ = [
    "BASE_TYPE_MAPPINGS",
    "AccountName",
    "AnyAsset",
    "AssetHbd",
    "AssetHive",
    "AssetHiveOrHbd",
    "AssetHiveOrVests",
    "AssetVests",
    "BlockId",
    "CustomIdType",
    "HardforkVersion",
    "Hex",
    "HiveDateTime",
    "HiveInt",
    "Int16t",
    "Int64t",
    "JsonString",
    "LegacyAnyAsset",
    "LegacyAssetHbd",
    "LegacyAssetHive",
    "LegacyAssetHiveOrHbd",
    "LegacyAssetHiveOrVests",
    "LegacyAssetVests",
    "NaiAsset",
    "OptionallyEmptyAccountName",
    "Permlink",
    "PublicKey",
    "Sha256",
    "Signature",
    "TransactionId",
    "Uint8t",
    "Uint16t",
    "Uint32t",
    "Uint64t",
    "Url",
    "Version",
    "WitnessUrl",
]


@dataclass(frozen=True, kw_only=True)
class NaiAsset:
    """Asset in HF26 (NAI) form, e.g. `{"amount": "1000", "precision": 3, "nai": "@@000000021"}`."""

    amount: int | str
    precision: int
    nai: str


# basic
AccountName: TypeAlias = str
OptionallyEmptyAccountName: TypeAlias = str
CustomIdType: TypeAlias = str
Permlink: TypeAlias = str
PublicKey: TypeAlias = str
Url: TypeAlias = str
WitnessUrl: TypeAlias = str

# hex
Hex: TypeAlias = str
Sha256: TypeAlias = str
Signature: TypeAlias = str
TransactionId: TypeAlias = str
BlockId: TypeAlias = str

# integers
Uint8t: TypeAlias = int
Int16t: TypeAlias = int
Uint16t: TypeAlias = int
Uint32t: TypeAlias = int
Int64t: TypeAlias = int | str
Uint64t: TypeAlias = int | str
HiveInt: TypeAlias = int | str

# time
HiveDateTime: TypeAlias = str

# version
Version: TypeAlias = str
HardforkVersion: TypeAlias = str

# json embedded in string
JsonString: TypeAlias = str

# assets - HF26 (NAI) form
AssetHive: TypeAlias = NaiAsset
AssetHbd: TypeAlias = NaiAsset
AssetVests: TypeAlias = NaiAsset
AssetHiveOrHbd: TypeAlias = NaiAsset
AssetHiveOrVests: TypeAlias = NaiAsset
AnyAsset: TypeAlias = NaiAsset

# assets - legacy form, e.g. "1.000 HIVE" (condenser_api, bridge)
LegacyAssetHive: TypeAlias = str
LegacyAssetHbd: TypeAlias = str
LegacyAssetVests: TypeAlias = str
LegacyAssetHiveOrHbd: TypeAlias = str
LegacyAssetHiveOrVests: TypeAlias = str
LegacyAnyAsset: TypeAlias = str


BASE_TYPE_MAPPINGS: Final[dict[str, str]] = {
    "AccountName": "schemas.fields.basic.AccountName",
    "OptionallyEmptyAccountName": "schemas.fields.basic.OptionallyEmptyAccountName",
    "CustomIdType": "schemas.fields.basic.CustomIdType",
    "Permlink": "schemas.fields.basic.Permlink",
    "PublicKey": "schemas.fields.basic.PublicKey",
    "Url": "schemas.fields.basic.Url",
    "WitnessUrl": "schemas.fields.basic.WitnessUrl",
    "Hex": "schemas.fields.hex.Hex",
    "Sha256": "schemas.fields.hex.Sha256",
    "Signature": "schemas.fields.hex.Signature",
    "TransactionId": "schemas.fields.hex.TransactionId",
    "BlockId": "schemas.fields.hex.BlockId",
    "Uint8t": "schemas.fields.integers.Uint8t",
    "Int16t": "schemas.fields.integers.Int16t",
    "Uint16t": "schemas.fields.integers.Uint16t",
    "Uint32t": "schemas.fields.integers.Uint32t",
    "Int64t": "schemas.fields.integers.Int64t",
    "Uint64t": "schemas.fields.integers.Uint64t",
    "HiveInt": "schemas.fields.hive_int.HiveInt",
    "HiveDateTime": "schemas.fields.hive_datetime.HiveDateTime",
    "Version": "schemas.fields.version.Version",
    "HardforkVersion": "schemas.fields.version.HardforkVersion",
    "JsonString": "schemas.fields.resolvables.JsonString",
    "AssetHive": "schemas.fields.assets.AssetHive",
    "AssetHbd": "schemas.fields.assets.AssetHbd",
    "AssetVests": "schemas.fields.assets.AssetVests",
    "AssetHiveOrHbd": "schemas.fields.resolvables.AssetUnionAssetHiveAssetHbd",
    "AssetHiveOrVests": "schemas.fields.resolvables.AssetUnionAssetHiveAssetVests",
    "AnyAsset": "schemas.fields.resolvables.AnyAsset",
    "LegacyAssetHive": "schemas.fields.assets.AssetHive",
    "LegacyAssetHbd": "schemas.fields.assets.AssetHbd",
    "LegacyAssetVests": "schemas.fields.assets.AssetVests",
    "LegacyAssetHiveOrHbd": "schemas.fields.resolvables.AssetUnionAssetHiveAssetHbd",
    "LegacyAssetHiveOrVests": "schemas.fields.resolvables.AssetUnionAssetHiveAssetVests",
    "LegacyAnyAsset": "schemas.fields.resolvables.AnyAsset",
}
