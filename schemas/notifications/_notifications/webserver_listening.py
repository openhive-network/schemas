from __future__ import annotations

from typing import Literal

from pydantic import Field

from schemas.notifications.abc.notification_base import NotificationBase
from msgspec import field


class WebserverListening(NotificationBase):
    type_: Literal["HTTP", "WS"] = field(name="type")
    address: str
    port: int

    @classmethod
    def get_notification_name(cls) -> str:
        return "webserver listening"
