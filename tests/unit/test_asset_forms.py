from __future__ import annotations

from typing import Final, NamedTuple

import msgspec
import pytest

from schemas.decoders import dec_hook_hf26
from schemas.encoders import enc_hook_hf26
from schemas.fields.assets import (
    AnyAsset,
    AssetBase,
    AssetHbd,
    AssetHive,
    AssetHiveOrHbd,
    AssetHiveOrVests,
    AssetTbd,
    AssetTests,
    AssetVests,
    LegacyAnyAsset,
    LegacyAssetHbd,
    LegacyAssetHive,
    LegacyAssetHiveOrHbd,
    LegacyAssetHiveOrVests,
    LegacyAssetVests,
)

NAI_HIVE = {"amount": "1000", "precision": 3, "nai": "@@000000021"}
NAI_HBD = {"amount": "2000", "precision": 3, "nai": "@@000000013"}
NAI_VESTS = {"amount": "3000000", "precision": 6, "nai": "@@000000037"}
LEGACY_HIVE = "1.000 HIVE"
LEGACY_HBD = "2.000 HBD"
LEGACY_VESTS = "3.000000 VESTS"


class Case(NamedTuple):
    asset_type: type[object]  # also abstract asset types (unions), which mypy rejects as `type[AssetBase]`
    value: object
    expected: AssetBase
    value_in_other_form: object


CASES: Final[dict[str, Case]] = {
    "AssetHive": Case(AssetHive, NAI_HIVE, AssetHive(amount=1000), LEGACY_HIVE),
    "AssetHbd": Case(AssetHbd, NAI_HBD, AssetHbd(amount=2000), LEGACY_HBD),
    "AssetVests": Case(AssetVests, NAI_VESTS, AssetVests(amount=3000000), LEGACY_VESTS),
    "AssetHiveOrHbd": Case(AssetHiveOrHbd, NAI_HBD, AssetHbd(amount=2000), LEGACY_HBD),
    "AssetHiveOrVests": Case(AssetHiveOrVests, NAI_VESTS, AssetVests(amount=3000000), LEGACY_VESTS),
    "AnyAsset": Case(AnyAsset, NAI_HIVE, AssetHive(amount=1000), LEGACY_HIVE),
    "LegacyAssetHive": Case(LegacyAssetHive, LEGACY_HIVE, AssetHive(amount=1000), NAI_HIVE),
    "LegacyAssetHbd": Case(LegacyAssetHbd, LEGACY_HBD, AssetHbd(amount=2000), NAI_HBD),
    "LegacyAssetVests": Case(LegacyAssetVests, LEGACY_VESTS, AssetVests(amount=3000000), NAI_VESTS),
    "LegacyAssetHiveOrHbd": Case(LegacyAssetHiveOrHbd, LEGACY_HBD, AssetHbd(amount=2000), NAI_HBD),
    "LegacyAssetHiveOrVests": Case(LegacyAssetHiveOrVests, LEGACY_VESTS, AssetVests(amount=3000000), NAI_VESTS),
    "LegacyAnyAsset": Case(LegacyAnyAsset, LEGACY_HIVE, AssetHive(amount=1000), NAI_HIVE),
}
ASSET_TYPES = pytest.mark.parametrize("case", CASES.values(), ids=CASES.keys())


def decode(asset_type: type[object], value: object) -> AssetBase:
    model = msgspec.defstruct("Model", [("asset", asset_type)])
    decoded = msgspec.convert({"asset": value}, model, dec_hook=dec_hook_hf26)
    asset: AssetBase = msgspec.structs.asdict(decoded)["asset"]
    return asset


def encode(asset: AssetBase) -> object:
    return msgspec.json.decode(msgspec.json.encode(asset, enc_hook=enc_hook_hf26))


@ASSET_TYPES
def test_asset_is_decoded_from_its_form(case: Case) -> None:
    # ACT
    decoded = decode(case.asset_type, case.value)

    # ASSERT
    assert isinstance(decoded, case.asset_type)
    assert decoded == case.expected


@ASSET_TYPES
def test_asset_is_not_decoded_from_the_other_form(case: Case) -> None:
    # ACT & ASSERT
    with pytest.raises(msgspec.ValidationError, match=r" - at `\$\.asset`$"):
        decode(case.asset_type, case.value_in_other_form)


@ASSET_TYPES
def test_asset_is_serialized_in_its_form(case: Case) -> None:
    # ARRANGE
    decoded = decode(case.asset_type, case.value)

    # ACT & ASSERT
    assert encode(decoded) == case.value


@pytest.mark.parametrize(
    ("asset_type", "value"),
    [
        (AssetHiveOrHbd, NAI_VESTS),
        (AssetHiveOrVests, NAI_HBD),
        (LegacyAssetHiveOrHbd, LEGACY_VESTS),
        (LegacyAssetHiveOrVests, LEGACY_HBD),
        (AssetHive, NAI_HBD),
        (LegacyAssetHive, LEGACY_HBD),
    ],
)
def test_asset_of_other_kind_is_rejected(asset_type: type[object], value: object) -> None:
    # ACT & ASSERT
    with pytest.raises(msgspec.ValidationError, match=r" - at `\$\.asset`$"):
        decode(asset_type, value)


@pytest.mark.parametrize("value", ["1.000 TESTS", "2.000 TBD"])
def test_legacy_asset_keeps_testnet_symbol(value: str) -> None:
    # ACT
    decoded = decode(LegacyAnyAsset, value)

    # ASSERT
    assert encode(decoded) == value


@pytest.mark.parametrize(
    ("asset", "expected"),
    [
        (AssetHive(amount=1000), LEGACY_HIVE),
        (AssetTests(amount=1000), "1.000 TESTS"),
        (AssetTbd(amount=2000), "2.000 TBD"),
        (AssetVests(amount=3000000), LEGACY_VESTS),
    ],
)
def test_asset_converted_to_legacy_form_is_serialized_as_legacy(asset: AssetBase, expected: str) -> None:
    # ACT
    legacy = asset.as_legacy_asset()

    # ASSERT
    assert isinstance(legacy, LegacyAnyAsset)
    assert legacy == asset
    assert encode(legacy) == expected


def test_testnet_assets_are_the_same_assets_as_mainnet_ones() -> None:
    # ACT & ASSERT
    assert isinstance(AssetHive(amount=1), AssetTests)
    assert isinstance(decode(LegacyAssetHive, "1.000 TESTS"), AssetTests)
    assert isinstance(AssetHbd(amount=1), AssetTbd)
    assert not isinstance(AssetHbd(amount=1), AssetTests)
