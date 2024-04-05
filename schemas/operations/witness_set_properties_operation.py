from __future__ import annotations

from pydantic import Field

from schemas.fields.basic import AccountName
from schemas.fields.compound import WitnessPropsSerialized
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class WitnessSetPropertiesOperation(Operation):
    __operation_name__ = "witness_set_properties"
    __offset__ = 42

    owner: AccountName
    props: WitnessPropsSerialized
    extensions: FutureExtensions = Field(default_factory=FutureExtensions)
