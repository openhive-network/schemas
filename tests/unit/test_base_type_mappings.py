from __future__ import annotations

import importlib
import subprocess
import sys
from typing import Any

import pytest

from schemas.fields import base_type_mappings
from schemas.fields._init_validators import InitValidator
from schemas.fields.base_type_mappings import BASE_TYPE_MAPPINGS


def resolve(path: str) -> Any:
    module, _, name = path.rpartition(".")
    return getattr(importlib.import_module(module), name)


def test_every_alias_has_mapping() -> None:
    # ARRANGE
    aliases = set(base_type_mappings.__all__) - {"BASE_TYPE_MAPPINGS", "NaiAsset"}

    # ACT & ASSERT
    assert aliases == set(BASE_TYPE_MAPPINGS)


@pytest.mark.parametrize("name", sorted(BASE_TYPE_MAPPINGS))
def test_mapping_resolves_to_validating_type(name: str) -> None:
    # ACT
    validating_type = resolve(BASE_TYPE_MAPPINGS[name])
    base_type = getattr(base_type_mappings, name)

    # ASSERT
    assert validating_type is not None
    if isinstance(validating_type, type) and issubclass(validating_type, InitValidator):
        covered = validating_type._covered_type()
        assert base_type is covered or covered in getattr(base_type, "__args__", ()), (name, base_type, covered)


def test_module_does_not_import_msgspec() -> None:
    # ACT
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "import sys, schemas.fields.base_type_mappings; "
            "print(sorted(m for m in sys.modules if m.startswith(('msgspec', 'schemas.'))))",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    # ASSERT
    assert result.stdout.strip() == "['schemas.fields', 'schemas.fields.base_type_mappings']"
