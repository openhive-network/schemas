from __future__ import annotations

from schemas.notification_model.notifications.abc.notification_base import NotificationBase
from schemas.notification_model.notifications.listening_notification import WebserverListening


class OpeningBeekeeperFailed(NotificationBase):
    pid: str
    connection: WebserverListening

    @classmethod
    def get_notification_name(cls) -> str:
        return "Opening beekeeper failed"
