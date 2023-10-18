from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class ExpiredAccountNotificationOperation(VirtualOperation):
    __operation_name__ = "expired_account_notification"
    __offset__ = 25

    account: AccountName
