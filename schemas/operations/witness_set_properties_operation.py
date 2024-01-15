from __future__ import annotations

from pydantic import Field

from schemas.fields.basic import AccountName
from schemas.fields.compound import LegacyChainProperties, LegacyChainPropertiesLegacy
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class _WitnessSetPropertiesOperation(Operation):
    __operation_name__ = "witness_set_properties"
    __offset__ = 42

    owner: AccountName
    extensions: FutureExtensions = Field(default_factory=FutureExtensions)


class WitnessSetPropertiesOperation(_WitnessSetPropertiesOperation):
    props: LegacyChainProperties


class WitnessSetPropertiesOperationLegacy(_WitnessSetPropertiesOperation):
    props: LegacyChainPropertiesLegacy
