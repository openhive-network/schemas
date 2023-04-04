from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName, AssetHiveHF26, LegacyChainProperties
from schemas.__private.preconfigured_base_model import Operation


class WitnessSetPropertiesOperation(Operation):
    witness: AccountName
    props: LegacyChainProperties[AssetHiveHF26]
