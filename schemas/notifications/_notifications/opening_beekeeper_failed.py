from __future__ import annotations

from schemas.notifications._notifications.webserver_listening import WebserverListening
from schemas.notifications.abc.notification_base import NotificationBase


class OpeningBeekeeperFailed(NotificationBase):
    pid: str
    connection: WebserverListening

    @classmethod
    def get_notification_name(cls) -> str:
        return "Opening beekeeper failed"
