from __future__ import annotations

from abc import ABC, abstractmethod

from schemas._preconfigured_base_model import PreconfiguredBaseModel


class NotificationBase(PreconfiguredBaseModel, ABC):
    @classmethod
    @abstractmethod
    def get_notification_name(cls) -> str:
        """Returns name of notification that following data structure is bind to"""
