from __future__ import annotations

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.notification_model.notifications.abc.notification_base import NotificationBase


class ClosedWalletDetail(PreconfiguredBaseModel):
    name: str
    unlocked: bool


class AttemptClosingWallets(NotificationBase):
    token: str
    wallets: list[ClosedWalletDetail]

    @classmethod
    def get_notification_name(cls) -> str:
        return "Attempt of closing all wallets"
