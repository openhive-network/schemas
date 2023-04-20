from __future__ import annotations

from schemas.__private.hive_fields_schemas_strict import AccountName, AssetHiveLegacy, Uint32t
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class CollateralizedConvertOperationStrict(PreconfiguredBaseModel):
    owner: AccountName
    request_id: Uint32t
    amount: AssetHiveLegacy
