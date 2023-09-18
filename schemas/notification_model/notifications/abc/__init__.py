from __future__ import annotations

from typing import TypeVar

from schemas.notification_model.notifications.error_notification import Error
from schemas.notification_model.notifications.listening_notification import WebserverListening
from schemas.notification_model.notifications.p2p_listening import P2PListening
from schemas.notification_model.notifications.status_notification import Status
from schemas.notification_model.notifications.switching_forks_notification import SwitchingForks

SupportedNotificationT = TypeVar(
    "SupportedNotificationT", bound=Error | WebserverListening | P2PListening | Status | SwitchingForks
)

__all__ = ["SupportedNotificationT", "Error", "WebserverListening", "P2PListening", "Status", "SwitchingForks"]
