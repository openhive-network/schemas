from __future__ import annotations

from abc import abstractmethod

from schemas._preconfigured_base_model import PreconfiguredBaseModel


class NotificationBase(PreconfiguredBaseModel):
    @classmethod
    @abstractmethod
    def get_notification_name(cls) -> str:
        """Returns name of notification that following data structure is bind to"""
