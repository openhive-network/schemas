from __future__ import annotations

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.notifications.abc.notification_base import NotificationBase


class ClosedWalletDetail(PreconfiguredBaseModel):
    name: str
    unlocked: bool


class AttemptClosingWallets(NotificationBase):
    token: str
    wallets: list[ClosedWalletDetail]

    @classmethod
    def get_notification_name(cls) -> str:
        return "Attempt of closing all wallets"
