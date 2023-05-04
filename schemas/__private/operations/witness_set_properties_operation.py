from __future__ import annotations

from typing import Generic

from pydantic.generics import GenericModel

from schemas.__private import LegacyChainProperties
from schemas.__private.hive_fields_schemas import AccountName, AssetHive
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class WitnessSetPropertiesOperation(PreconfiguredBaseModel, GenericModel, Generic[AssetHive]):
    witness: AccountName
    props: LegacyChainProperties
