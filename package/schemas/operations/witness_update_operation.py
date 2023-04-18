from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel

if TYPE_CHECKING:
    from schemas.__private.hive_fields_schemas import (
        AccountName,
        AssetHiveLegacy,
        LegacyChainProperties,
        PublicKey,
    )
    from schemas.types import AssetHive


class WitnessUpdateOperation(PreconfiguredBaseModel):
    owner: AccountName
    url: str
    block_signing_key: PublicKey
    props: LegacyChainProperties
    fee: AssetHive | AssetHiveLegacy  # currently ignored but validated
