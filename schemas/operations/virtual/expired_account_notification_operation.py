from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class ExpiredAccountNotificationOperation(VirtualOperation):
    account: AccountName

    @classmethod
    def get_name(cls):
        return "expired_account_notification"
    
    @classmethod
    def offset(cls):
        return 25
