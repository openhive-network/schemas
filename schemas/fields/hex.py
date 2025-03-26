from __future__ import annotations

from typing import Annotated

import msgspec

__all__ = [
    "Hex",
    "Sha256",
    "Signature",
    "TransactionId",
]


# class Hex(ConstrainedStr):

Hex = Annotated[str, msgspec.Meta(pattern=r"^[0-9a-fA-F]*$")]


# class Sha256(Hex):

Sha256 = Annotated[Hex, msgspec.Meta(min_length=64, max_length=64)]

# class Signature(Hex):

Signature = Annotated[Hex, msgspec.Meta(min_length=130, max_length=130)]

# class TransactionId(Hex):

TransactionId = Annotated[Hex, msgspec.Meta(min_length=40, max_length=40)]
