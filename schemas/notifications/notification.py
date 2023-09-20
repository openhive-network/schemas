from __future__ import annotations

from datetime import datetime  # noqa: TCH003
from typing import Any, Generic

from pydantic.generics import GenericModel

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.notifications._known_notifications import KnownNotificationT


class Notification(PreconfiguredBaseModel, GenericModel, Generic[KnownNotificationT]):
    name: str
    time: datetime
    value: KnownNotificationT

    @staticmethod
    def factory(t: type[KnownNotificationT], **kwargs: Any) -> Notification[KnownNotificationT]:
        response_cls = Notification[t]  # type: ignore[valid-type]
        response_cls.update_forward_refs(**locals())
        return response_cls(**kwargs)
