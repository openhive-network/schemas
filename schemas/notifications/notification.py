from __future__ import annotations

from datetime import datetime  # noqa: TCH003
from typing import Any, Generic

from pydantic.generics import GenericModel

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.notifications import KnownNotificationT


class Notification(PreconfiguredBaseModel, GenericModel, Generic[KnownNotificationT]):
    name: str
    time: datetime
    value: KnownNotificationT

    @staticmethod
    def factory(
        expected_model: type[KnownNotificationT] | None = None, **kwargs: Any
    ) -> Notification[KnownNotificationT]:
        response_cls = Notification[expected_model] if expected_model else Notification[KnownNotificationT]  # type: ignore[valid-type]
        response_cls.update_forward_refs(**locals())  # type: ignore[attr-defined]
        return response_cls(**kwargs)  # type: ignore[return-value]
