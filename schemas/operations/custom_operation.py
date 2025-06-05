from __future__ import annotations

from msgspec import field

from schemas.fields.basic import AccountName
from schemas.fields.hex import Hex
from schemas.fields.integers import Uint16t
from schemas.operation import Operation


class CustomOperation(Operation, kw_only=True):
    required_auths: list[AccountName]
    id_: Uint16t = field(name="id")
    data: Hex

    @classmethod
    def get_name(cls) -> str:
        return "custom"

    @classmethod
    def offset(cls) -> int:
        return 15
