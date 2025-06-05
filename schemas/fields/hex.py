from __future__ import annotations

from typing import TYPE_CHECKING

import msgspec

from schemas.fields._init_validators import ValidatorString

__all__ = [
    "Hex",
    "Sha256",
    "Signature",
    "TransactionId",
]

if TYPE_CHECKING:
    Hex = str
    Sha256 = str
    Signature = str
    TransactionId = str
else:
    Hex = ValidatorString.factory("Hex", msgspec.Meta(pattern=r"^[0-9a-fA-F]*$"))
    Sha256 = ValidatorString.factory("Sha256", msgspec.Meta(min_length=64, max_length=64))
    Signature = ValidatorString.factory("Signature", msgspec.Meta(min_length=130, max_length=130))
    TransactionId = ValidatorString.factory("TransactionId", msgspec.Meta(min_length=40, max_length=40))
