from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class ExpiredAccountNotificationOperation(VirtualOperation):
    account: AccountName

    @classmethod
    def get_name(cls) -> str:
        return "expired_account_notification"

    @classmethod
    def vop_offset(cls) -> int:
        return 25
