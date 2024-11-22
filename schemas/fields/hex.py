from __future__ import annotations

import re

from pydantic import StringConstraints

__all__ = [
    "Hex",
    "Sha256",
    "Signature",
    "TransactionId",
]


class Hex(StringConstraints):
    regex = re.compile(r"^[0-9a-fA-F]*$")


class Sha256(Hex):
    min_length = 64
    max_length = 64


class Signature(Hex):
    min_length = 130
    max_length = 130


class TransactionId(Hex):
    min_length = 40
    max_length = 40
