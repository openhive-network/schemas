from __future__ import annotations

from typing import TYPE_CHECKING

import msgspec
import pytest

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.decoders import dec_hook_hf26
from schemas.errors import FieldValidationError, SchemaBaseError
from schemas.fields.assets import AssetHive, LegacyAssetHive
from schemas.fields.basic import AccountName
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.fields.integers import Uint64t
from schemas.fields.json_string import JsonString

if TYPE_CHECKING:
    from collections.abc import Callable


class Fields(PreconfiguredBaseModel):
    assets: list[AssetHive] | None = None
    legacy_assets: list[LegacyAssetHive] | None = None
    ints: list[HiveInt] | None = None
    uints: list[Uint64t] | None = None
    dates: list[HiveDateTime] | None = None
    names: list[AccountName] | None = None
    jsons: list[JsonString[object]] | None = None


@pytest.mark.parametrize(
    "create",
    [
        lambda: AccountName("Invalid!"),
        lambda: HiveInt("not a number"),
        lambda: HiveInt(1.5),
        lambda: Uint64t(-1),
        lambda: HiveDateTime("2020-01-01"),
        lambda: HiveDateTime(5),  # type: ignore[arg-type]
        lambda: AssetHive.from_legacy("1.000 HBD"),
        lambda: AssetHive.from_legacy("-1.000 HIVE"),
        lambda: AssetHive.from_nai({"amount": "1", "precision": 3, "nai": "@@000000013"}),
        lambda: JsonString("{not json"),
    ],
)
def test_field_types_raise_field_validation_error(create: Callable[[], object]) -> None:
    # ACT & ASSERT
    with pytest.raises(FieldValidationError) as error:
        create()
    assert isinstance(error.value, SchemaBaseError)
    assert isinstance(error.value, msgspec.ValidationError)
    assert isinstance(error.value, ValueError)


@pytest.mark.parametrize(
    ("data", "expected_path"),
    [
        ({"assets": [{"amount": "1", "precision": 3, "nai": "@@000000013"}]}, "$.assets[0]"),
        ({"legacy_assets": ["1.000 HBD"]}, "$.legacy_assets[0]"),
        ({"legacy_assets": [5]}, "$.legacy_assets[0]"),
        ({"ints": [1, "not a number"]}, "$.ints[1]"),
        ({"uints": [-1]}, "$.uints[0]"),
        ({"dates": ["2020-01-01"]}, "$.dates[0]"),
        ({"names": ["alice", "Invalid!"]}, "$.names[1]"),
        ({"jsons": ["{not json"]}, "$.jsons[0]"),
    ],
)
def test_invalid_field_is_reported_by_msgspec_with_its_location(data: dict[str, object], expected_path: str) -> None:
    # ACT & ASSERT
    with pytest.raises(msgspec.ValidationError) as error:
        msgspec.convert(data, Fields, dec_hook=dec_hook_hf26)
    assert str(error.value).endswith(f" - at `{expected_path}`")
