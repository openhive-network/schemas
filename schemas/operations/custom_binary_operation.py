from __future__ import annotations

from msgspec import field

from schemas.fields.basic import AccountName, CustomIdType
from schemas.fields.compound import Authority
from schemas.operation import Operation


class CustomBinaryOperation(Operation, kw_only=True):
    required_owner_auths: list[AccountName]
    required_active_auths: list[AccountName]
    required_posting_auths: list[AccountName]
    required_auths: list[Authority]
    id_: CustomIdType = field(name="id")
    data: list[str]

    @classmethod
    def get_name(cls) -> str:
        return "custom_binary"

    @classmethod
    def offset(cls) -> int:
        return 35
