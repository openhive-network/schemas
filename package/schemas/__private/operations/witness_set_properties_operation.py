from __future__ import annotations

from schemas.__private.hive_fields_schemas import AccountName, LegacyChainProperties
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class WitnessSetPropertiesOperation(PreconfiguredBaseModel):
    witness: AccountName
    props: LegacyChainProperties
