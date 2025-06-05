from __future__ import annotations

from msgspec import field

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.app_status_api.fundaments_of_responses import ForkItem, KnownRecords, KnownWebservers, StatusItem
from schemas.fields.hive_datetime import HiveDateTime


class GetAppStatus(PreconfiguredBaseModel):
    last_update: HiveDateTime
    records: KnownRecords = field(default_factory=lambda: KnownRecords())
    webservers: KnownWebservers = field(default_factory=lambda: KnownWebservers())
    statuses: list[StatusItem] = field(default_factory=list)
    forks: list[ForkItem] = field(default_factory=list)
