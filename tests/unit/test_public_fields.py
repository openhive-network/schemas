from __future__ import annotations

import subprocess
import sys
import typing
from typing import Final

import pytest

from schemas.fields import public, validation
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.public import _fields as public_aliases

FIELD_TYPES: Final[list[str]] = sorted(public_aliases.__all__)
"""Names of the field types - aliases of `schemas.fields.public`."""
NAI_ASSETS: Final[list[str]] = ["AnyAsset", "AssetHbd", "AssetHive", "AssetHiveOrHbd", "AssetHiveOrVests", "AssetVests"]
LEGACY_ASSETS: Final[list[str]] = [f"Legacy{name}" for name in NAI_ASSETS]
OF_BUILTINS: Final[list[str]] = sorted(set(FIELD_TYPES) - {*NAI_ASSETS, *LEGACY_ASSETS, "HiveDateTime"})


def test_package_exports_every_alias() -> None:
    # ACT & ASSERT
    assert set(public.__all__) >= set(FIELD_TYPES)


@pytest.mark.parametrize("name", FIELD_TYPES)
def test_alias_has_the_form_of_the_same_name(name: str) -> None:
    # ACT & ASSERT
    assert name in validation.__all__


def builtin_of(form: object) -> object:
    """The builtin a form is made of - of its first member for unions (e.g. `int | Annotated[str, ...]`)."""
    if typing.get_origin(form) is typing.Union:
        form = typing.get_args(form)[0]
    return typing.get_args(form)[0] if typing.get_origin(form) is typing.Annotated else form


@pytest.mark.parametrize("name", OF_BUILTINS)
def test_alias_is_the_builtin_of_the_form(name: str) -> None:
    # ACT
    alias = getattr(public, name)

    # ASSERT
    assert alias is builtin_of(getattr(validation, name))


def test_alias_of_dates_is_the_user_friendly_date() -> None:
    # ACT & ASSERT
    assert public.HiveDateTime is HiveDateTime


@pytest.mark.parametrize(
    ("name", "legacy"), [(name, False) for name in NAI_ASSETS] + [(name, True) for name in LEGACY_ASSETS]
)
def test_assets_are_mapped_to_types_of_their_form(name: str, *, legacy: bool) -> None:
    # ACT
    form = getattr(validation, name)

    # ASSERT
    if legacy:
        assert typing.get_origin(form) is typing.Annotated
        assert typing.get_args(form)[0] is str
    else:
        assert isinstance(form, type)
        assert issubclass(form, validation.AnyAsset)
    assert getattr(public, name) is public.Asset


@pytest.mark.parametrize(
    "class_",
    [
        public.Asset,
        public.AssetFactory,
        public.AssetInfo,
        public.AssetKind,
        public.SatoshiFactory,
        public.TokensFactory,
    ],
)
def test_classes_are_of_the_package_not_of_its_private_modules(class_: type) -> None:
    """Generators import types from their module (`__module__`) - classes are imported from the package."""
    # ACT & ASSERT
    assert class_.__module__ == public.__name__


def test_package_does_not_import_msgspec() -> None:
    # ACT
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "import sys, schemas.fields.public; "
            "print(sorted(m for m in sys.modules if m.startswith(('msgspec', 'schemas.'))))",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    # ASSERT
    assert result.stdout.strip() == (
        "['schemas.fields', 'schemas.fields.hive_datetime', 'schemas.fields.public', "
        "'schemas.fields.public._asset_info', 'schemas.fields.public._assets', 'schemas.fields.public._fields', "
        "'schemas.fields.serializable', 'schemas.hive_constants']"
    )
