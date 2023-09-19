from __future__ import annotations

from datetime import datetime  # noqa: TCH003
from typing import Any, Generic

from pydantic.generics import GenericModel

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.notifications.abc import SupportedNotificationT


class Notification(PreconfiguredBaseModel, GenericModel, Generic[SupportedNotificationT]):
    name: str
    time: datetime
    value: SupportedNotificationT

    @staticmethod
    def factory(t: type[SupportedNotificationT], **kwargs: Any) -> Notification[SupportedNotificationT]:
        response_cls = Notification[t]  # type: ignore[valid-type]
        response_cls.update_forward_refs(**locals())
        return response_cls(**kwargs)
