from __future__ import annotations

from schemas.fields.assets.hive import AssetHiveHF26
from schemas.fields.basic import AccountName, LegacyChainProperties
from schemas.operation import Operation


class WitnessSetPropertiesOperation(Operation):
    __operation_name__ = "witness_set_properties"

    witness: AccountName
    props: LegacyChainProperties[AssetHiveHF26]
