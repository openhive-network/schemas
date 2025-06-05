from __future__ import annotations

from typing import Literal

from msgspec import field

from schemas.notifications.abc.notification_base import NotificationBase


class WebserverListening(NotificationBase):
    type_: Literal["HTTP", "WS"] = field(name="type")
    address: str
    port: int

    @classmethod
    def get_notification_name(cls) -> str:
        return "webserver listening"
