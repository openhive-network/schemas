"""
Builtin counterparts of the field types - for public models generated in `hiveio_api`.

Every alias below is named exactly like the field type it stands for (its form of validation models in
`schemas.fields.validation` has the same name), but resolves to plain python types (the form in which the value appears
in raw JSON) - except assets, which resolve to the user-friendly `Asset` of both JSON forms, dates, which are the
user-friendly `HiveDateTime` (an aware `datetime`) itself, and integers of 64 bits (`Int64t`, `Uint64t`, `HiveInt`),
which are `int` also when hived sends them as strings (values not fitting doubles of JSON). Generated public API models
use these aliases, so they carry the semantic name without importing any validation machinery.

This module must stay import-light (no msgspec, no other schemas modules than the import-light `_assets` and
`schemas.fields.hive_datetime`).
"""

# ruff: noqa: UP040
# Aliases intentionally use `TypeAlias` (not the `type` statement) - at runtime they must be the plain types,
# so generated models resolve them to builtins.
from __future__ import annotations

from typing import TypeAlias

from schemas.fields.hive_datetime import HiveDateTime

from ._assets import Asset

__all__ = [
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
    "Version",
    "WitnessUrl",
]


# basic
AccountName: TypeAlias = str
OptionallyEmptyAccountName: TypeAlias = str
CustomIdType: TypeAlias = str
Permlink: TypeAlias = str
PublicKey: TypeAlias = str
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
Int64t: TypeAlias = int
Uint64t: TypeAlias = int
HiveInt: TypeAlias = int

# version
Version: TypeAlias = str
HardforkVersion: TypeAlias = str

# json embedded in string
JsonString: TypeAlias = str

# assets - one user-friendly type of both forms; the name tells the form of the field: NAI (HF26), e.g.
# {"amount": "1000", "precision": 3, "nai": "@@000000021"}, or legacy, e.g. "1.000 HIVE" (condenser_api, bridge)
AssetHive: TypeAlias = Asset
AssetHbd: TypeAlias = Asset
AssetVests: TypeAlias = Asset
AssetHiveOrHbd: TypeAlias = Asset
AssetHiveOrVests: TypeAlias = Asset
AnyAsset: TypeAlias = Asset
LegacyAssetHive: TypeAlias = Asset
LegacyAssetHbd: TypeAlias = Asset
LegacyAssetVests: TypeAlias = Asset
LegacyAssetHiveOrHbd: TypeAlias = Asset
LegacyAssetHiveOrVests: TypeAlias = Asset
LegacyAnyAsset: TypeAlias = Asset
