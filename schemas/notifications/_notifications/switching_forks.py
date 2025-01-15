from __future__ import annotations

from pydantic import Field

from schemas.notifications.abc.notification_base import NotificationBase
from msgspec import field


class SwitchingForks(NotificationBase):
    id_: str = field(name="id")
    num: int

    @classmethod
    def get_notification_name(cls) -> str:
        return "switching forks"
