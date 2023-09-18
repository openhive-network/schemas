from __future__ import annotations

from typing import Literal

from pydantic import Field

from schemas.notification_model.notifications.abc.notification_base import NotificationBase


class WebserverListening(NotificationBase):
    type_: Literal["HTTP", "WS"] = Field(alias="type")
    address: str
    port: int

    @classmethod
    def get_notification_name(cls) -> str:
        return "webserver listening"
