from __future__ import annotations

from datetime import datetime  # noqa: TCH003
from typing import Any, Generic

from pydantic.generics import GenericModel

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.notifications import KnownNotificationT
from schemas.notifications.abc import SupportedNotificationT


class Notification(PreconfiguredBaseModel, GenericModel, Generic[SupportedNotificationT]):
    name: str
    time: datetime
    value: SupportedNotificationT

    @staticmethod
    def factory(
        expected_model: type[KnownNotificationT] | None = None, **kwargs: Any
    ) -> Notification[KnownNotificationT]:
        response_cls = Notification[expected_model] if expected_model else Notification[KnownNotificationT]  # type: ignore[valid-type]
        response_cls.update_forward_refs(**locals())
        return response_cls(**kwargs)
