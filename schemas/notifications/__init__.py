from __future__ import annotations

from typing import TypeVar

from schemas.notifications._notifications import (
    AttemptClosingWallets,
    Error,
    OpeningBeekeeperFailed,
    P2PListening,
    Status,
    SwitchingForks,
    WebserverListening,
)
from schemas.notifications.notification import Notification

KnownNotificationT = TypeVar(
    "KnownNotificationT",
    AttemptClosingWallets,
    Error,
    OpeningBeekeeperFailed,
    P2PListening,
    Status,
    SwitchingForks,
    WebserverListening,
)


__all__ = [
    "KnownNotificationT",
    "Notification",
    # NOTIFICATIONS
    "AttemptClosingWallets",
    "Error",
    "OpeningBeekeeperFailed",
    "P2PListening",
    "Status",
    "SwitchingForks",
    "WebserverListening",
]
