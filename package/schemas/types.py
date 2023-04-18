from __future__ import annotations

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import (
        AssetHbdLegacy,
        AssetHbdNai,
        AssetHiveLegacy,
        AssetHiveNai,
        AssetVestsLegacy,
        AssetVestsNai,
    )

    AssetHbd: TypeAlias = AssetHbdNai | AssetHbdLegacy
    AssetHive: TypeAlias = AssetHiveNai | AssetHiveLegacy
    AssetVests: TypeAlias = AssetVestsNai | AssetVestsLegacy
