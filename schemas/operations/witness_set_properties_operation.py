from __future__ import annotations

from msgspec import field

from schemas.fields.basic import AccountName
from schemas.fields.compound import WitnessProps, WitnessPropsSerialized
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class WitnessSetPropertiesCommon(Operation):
    owner: AccountName
    extensions: FutureExtensions = field(default_factory=FutureExtensions)

    @classmethod
    def get_name(cls) -> str:
        return "witness_set_properties"

    @classmethod
    def offset(cls) -> int:
        return 42


class WitnessSetPropertiesOperation(WitnessSetPropertiesCommon, kw_only=True):
    """Actual model accepted by blockchain. Props be created using the `serialize_set_properties` util executable."""

    props: WitnessPropsSerialized


class _WitnessSetPropertiesOperationFactory(WitnessSetPropertiesCommon, kw_only=True):
    """Model used to create a model of the operation before serializing props"""

    props: WitnessProps


class WitnessSetPropertiesOperationFactory(_WitnessSetPropertiesOperationFactory):
    ...


class WitnessSetPropertiesOperationFactoryLegacy(_WitnessSetPropertiesOperationFactory):
    ...
