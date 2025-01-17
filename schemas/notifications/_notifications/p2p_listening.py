from __future__ import annotations

from typing import Literal


from schemas.notifications.abc.notification_base import NotificationBase
from msgspec import field


class P2PListening(NotificationBase):
    type_: Literal["p2p"] = field(name="type")
    address: str
    port: int

    @classmethod
    def get_notification_name(cls) -> str:
        return "P2P listening"
