from __future__ import annotations

from schemas.notifications.abc.notification_base import NotificationBase


class Error(NotificationBase):
    message: str

    @classmethod
    def get_notification_name(cls) -> str:
        return "error"
