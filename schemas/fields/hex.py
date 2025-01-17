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
#     regex = re.compile(r"^[0-9a-fA-F]*$")

Hex = Annotated[str, msgspec.Meta(pattern=r"^[0-9a-fA-F]*$")]


# class Sha256(Hex):
#     min_length = 64
#     max_length = 64

Sha256 = Annotated[Hex, msgspec.Meta(min_length=64, max_length=64)]

# class Signature(Hex):
#     min_length = 130
#     max_length = 130

Signature = Annotated[Hex, msgspec.Meta(min_length=130, max_length=130)]

# class TransactionId(Hex):
#     min_length = 40
#     max_length = 40

TransactionId = Annotated[Hex, msgspec.Meta(min_length=40, max_length=40)]
