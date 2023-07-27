from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import (
    AssetHbd,
    AssetHbdHF26,
    AssetHbdLegacy,
    AssetHive,
    AssetHiveHF26,
    AssetHiveLegacy,
    AssetVests,
    AssetVestsHF26,
    AssetVestsLegacy,
)
from schemas.__private.operations._operation_type import OperationType
from schemas.__private.operations.virtual import VirtualOperationType

Hf26OperationType = OperationType[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]
LegacyOperationType = OperationType[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]

Hf26VirtualOperationType = VirtualOperationType[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]
LegacyVirtualOperationType = VirtualOperationType[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]

AllOperationType = (
    OperationType[AssetHive, AssetHbd, AssetVests] | VirtualOperationType[AssetHive, AssetHbd, AssetVests]
)

Hf26AllOperationType = AllOperationType[AssetHiveHF26, AssetHbdHF26, AssetVestsHF26]
LegacyAllOperationType = AllOperationType[AssetHiveLegacy, AssetHbdLegacy, AssetVestsLegacy]

__all__ = [
    "AllOperationType",
    "Hf26AllOperationType",
    "Hf26OperationType",
    "Hf26VirtualOperationType",
    "LegacyAllOperationType",
    "LegacyOperationType",
    "LegacyVirtualOperationType",
]
