from __future__ import annotations

from typing import Generic

from pydantic import Field
from pydantic.generics import GenericModel

from schemas.fields.basic import AccountName
from schemas.fields.compound import WitnessProps, WitnessPropsSerialized
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class WitnessSetPropertiesCommon(Operation):
    __operation_name__ = "witness_set_properties"
    __offset__ = 42

    owner: AccountName
    extensions: FutureExtensions = Field(default_factory=FutureExtensions)


class WitnessSetPropertiesOperation(WitnessSetPropertiesCommon, kw_only=True):
    """Actual model accepted by blockchain. Props be created using the `serialize_set_properties` util executable."""

    props: WitnessPropsSerialized


class _WitnessSetPropertiesOperationFactory(WitnessSetPropertiesCommon, kw_only=True):
    """Model used to create a model of the operation before serializing props"""

    props: WitnessProps


class WitnessSetPropertiesOperationFactory(_WitnessSetPropertiesOperationFactory):
    ...


class WitnessSetPropertiesOperationFactoryLegacy(
    _WitnessSetPropertiesOperationFactory
):
    ...
