from __future__ import annotations

from typing import TypeVar

from schemas.notification_model.notifications.abc.notification_base import NotificationBase
from schemas.notification_model.notifications.attempt_closing_wallets import AttemptClosingWallets
from schemas.notification_model.notifications.error_notification import Error
from schemas.notification_model.notifications.listening_notification import WebserverListening
from schemas.notification_model.notifications.opening_beekeeper_failed import OpeningBeekeeperFailed
from schemas.notification_model.notifications.p2p_listening import P2PListening
from schemas.notification_model.notifications.status_notification import Status
from schemas.notification_model.notifications.switching_forks_notification import SwitchingForks

SupportedNotificationT = TypeVar("SupportedNotificationT", bound=NotificationBase)
AllowedNotificationT = TypeVar(
    "AllowedNotificationT",
    bound=Error
    | WebserverListening
    | P2PListening
    | Status
    | SwitchingForks
    | AttemptClosingWallets
    | OpeningBeekeeperFailed
    | NotificationBase,
)

__all__ = [
    "SupportedNotificationT",
    "AllowedNotificationT",
    "Error",
    "WebserverListening",
    "P2PListening",
    "Status",
    "SwitchingForks",
    "AttemptClosingWallets",
    "OpeningBeekeeperFailed",
]
