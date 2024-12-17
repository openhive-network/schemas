from __future__ import annotations

from datetime import datetime  # noqa: TCH003

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.notifications._notifications import (
    AttemptClosingWallets,
    Error,
    OpeningBeekeeperFailed,
    P2PListening,
    Status,
    SwitchingForks,
    WebserverListening,
)

TAG_FIELD = "name"


class NotificationBase(PreconfiguredBaseModel):
    time: datetime


class AttemptClosingWalletsNotification(
    NotificationBase, tag_field=TAG_FIELD, tag=AttemptClosingWallets.get_notification_name()
):
    value: AttemptClosingWallets


class ErrorNotification(NotificationBase, tag_field=TAG_FIELD, tag=Error.get_notification_name()):
    value: Error


class OpeningBeekeeperFailedNotification(
    NotificationBase, tag_field=TAG_FIELD, tag=OpeningBeekeeperFailed.get_notification_name()
):
    value: OpeningBeekeeperFailed


class P2PListeningNotification(NotificationBase, tag_field=TAG_FIELD, tag=P2PListening.get_notification_name()):
    value: P2PListening


class StatusNotification(NotificationBase, tag_field=TAG_FIELD, tag=Status.get_notification_name()):
    value: Status


class SwitchingForksNotification(NotificationBase, tag_field=TAG_FIELD, tag=SwitchingForks.get_notification_name()):
    value: SwitchingForks


class WebserverListeningNotification(
    NotificationBase, tag_field=TAG_FIELD, tag=WebserverListening.get_notification_name()
):
    value: WebserverListening


KnownNotificationT = (
    AttemptClosingWalletsNotification
    | ErrorNotification
    | OpeningBeekeeperFailedNotification
    | P2PListeningNotification
    | StatusNotification
    | SwitchingForksNotification
    | WebserverListeningNotification
)
