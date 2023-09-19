from __future__ import annotations

from schemas.notifications.abc.notification_base import NotificationBase


class Status(NotificationBase):
    current_status: str

    @classmethod
    def get_notification_name(cls) -> str:
        return "hived_status"
