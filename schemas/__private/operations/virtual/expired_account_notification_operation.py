from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName
from schemas.__private.virtual_operation import VirtualOperation


class ExpiredAccountNotificationOperation(VirtualOperation):
    __operation_name__ = "expired_account_notification"

    account: AccountName
