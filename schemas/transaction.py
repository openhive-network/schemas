from __future__ import annotations

from copy import deepcopy
from typing import TYPE_CHECKING, Any, TypeVar

from typing_extensions import Self

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.hex import Signature, TransactionId
from schemas.fields.hive_datetime import HiveDateTime
from schemas.fields.hive_int import HiveInt
from schemas.operations import (
    Hf26OperationRepresentation,
    Hf26Operations,
    LegacyOperationRepresentation,
    LegacyOperations,
    convert_to_representation,
    convert_to_representation_legacy,
)

if TYPE_CHECKING:
    from schemas.decoders import DecoderFactory


__all__ = [
    "Transaction",
    "TransactionLegacy",
    "TransactionT",
]


class TransactionCommon(PreconfiguredBaseModel):
    ref_block_num: HiveInt
    ref_block_prefix: HiveInt
    expiration: HiveDateTime
    extensions: list[Any]
    signatures: list[Signature]


class Transaction(TransactionCommon):
    operations: list[Hf26OperationRepresentation]


class TransactionLegacy(TransactionCommon):
    operations: list[LegacyOperationRepresentation]
    block_num: HiveInt
    transaction_id: TransactionId
    transaction_num: HiveInt


class TransactionUserFriendly(Transaction):
    operations: list[Hf26Operations]  # type: ignore[assignment]

    def _get_object_for_serialization(self) -> Self:
        copied = deepcopy(self)
        copied.operations = [convert_to_representation(op) for op in self.operations]  # type: ignore[misc]
        return copied

    @classmethod
    def parse_raw(cls, raw: str, custom_decoder_factory: DecoderFactory | None = None) -> Self:
        # Default decoder is hf26_decoder
        if custom_decoder_factory is None:
            from schemas.decoders import get_hf26_decoder

            custom_decoder_factory = get_hf26_decoder
        parsed = Transaction.parse_raw(raw, custom_decoder_factory=custom_decoder_factory)
        shallowed = parsed.shallow_dict()
        shallowed.pop("operations")
        return cls(operations=[repr_op.value for repr_op in parsed.operations], **shallowed)


class TransactionLegacyUserFriendly(TransactionLegacy):
    operations: list[LegacyOperations]  # type: ignore[assignment]

    def _get_object_for_serialization(self) -> Self:
        copied = deepcopy(self)
        copied.operations = [convert_to_representation_legacy(op) for op in self.operations]  # type: ignore[misc]
        return copied

    @classmethod
    def parse_raw(cls, raw: str, custom_decoder_factory: DecoderFactory | None = None) -> Self:
        # Default decoder is hf26_decoder
        if custom_decoder_factory is None:
            from schemas.decoders import get_hf26_decoder

            custom_decoder_factory = get_hf26_decoder
        parsed = TransactionLegacy.parse_raw(raw, custom_decoder_factory=custom_decoder_factory)
        shallowed = parsed.shallow_dict()
        shallowed.pop("operations")
        return cls(operations=[repr_op.value for repr_op in parsed.operations], **shallowed)


TransactionT = TypeVar("TransactionT", bound=Transaction | TransactionLegacy)
