from __future__ import annotations

from typing import Literal

from msgspec import field

from schemas.fields.basic import AccountName
from schemas.fields.compound import WitnessProps
from schemas.fields.hex import Hex
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


WitnessPropsSerializedKey = Literal[
    "account_creation_fee",
    "account_subsidy_budget",
    "account_subsidy_decay",
    "key",
    "maximum_block_size",
    "new_signing_key",
    "sbd_exchange_rate",
    "sbd_interest_rate",
    "url",
    "hbd_exchange_rate",
    "hbd_interest_rate",
]


class WitnessSetPropertiesOperation(WitnessSetPropertiesCommon, kw_only=True):
    """Actual model accepted by blockchain. Props be created using the `serialize_set_properties` util executable."""

    props: list[tuple[WitnessPropsSerializedKey, Hex]]


class _WitnessSetPropertiesOperationFactory(WitnessSetPropertiesCommon, kw_only=True):
    """Model used to create a model of the operation before serializing props"""

    props: WitnessProps


class WitnessSetPropertiesOperationFactory(_WitnessSetPropertiesOperationFactory):
    ...


class WitnessSetPropertiesOperationFactoryLegacy(_WitnessSetPropertiesOperationFactory):
    ...
