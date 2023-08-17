from __future__ import annotations

from datetime import datetime  # noqa: TCH003
from typing import Any, Generic

from pydantic.generics import GenericModel

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.notification_model.notifications import AllowedNotificationT


class Notification(PreconfiguredBaseModel, GenericModel, Generic[AllowedNotificationT]):
    name: str
    time: datetime
    value: AllowedNotificationT

    @staticmethod
    def factory(t: type[AllowedNotificationT], **kwargs: Any) -> Notification[AllowedNotificationT]:
        response_cls = Notification[t]  # type: ignore[valid-type]
        response_cls.update_forward_refs(**locals())
        return response_cls(**kwargs)
