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
