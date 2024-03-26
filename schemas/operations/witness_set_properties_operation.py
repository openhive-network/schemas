from __future__ import annotations

from pydantic import Field

from schemas.fields.assets import AssetHbdHF26, AssetHiveHF26
from schemas.fields.basic import AccountName
from schemas.fields.compound import PropsWitnessSetProperties
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class WitnessSetPropertiesOperation(Operation):
    __operation_name__ = "witness_set_properties"
    __offset__ = 42

    owner: AccountName
    props: list[PropsWitnessSetProperties[AssetHiveHF26, AssetHbdHF26]]
    extensions: FutureExtensions = Field(default_factory=FutureExtensions)
