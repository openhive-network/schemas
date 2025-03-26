from __future__ import annotations

from msgspec import field

from schemas.notifications.abc.notification_base import NotificationBase


class SwitchingForks(NotificationBase):
    id_: str = field(name="id")
    num: int

    @classmethod
    def get_notification_name(cls) -> str:
        return "switching forks"
