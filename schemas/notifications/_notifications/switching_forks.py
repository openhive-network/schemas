from __future__ import annotations

from pydantic import Field

from schemas.notifications.abc.notification_base import NotificationBase


class SwitchingForks(NotificationBase):
    id_: str = Field(alias="id")
    num: int

    @classmethod
    def get_notification_name(cls) -> str:
        return "switching forks"
