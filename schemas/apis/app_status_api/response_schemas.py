from __future__ import annotations

from pydantic import Field

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.app_status_api.fundaments_of_responses import ForkItem, KnownRecords, KnownWebservers, StatusItem
from schemas.fields.hive_datetime import HiveDateTime


class GetAppStatus(PreconfiguredBaseModel):
    last_update: HiveDateTime
    records: KnownRecords = Field(default_factory=lambda: KnownRecords())
    webservers: KnownWebservers = Field(default_factory=lambda: KnownWebservers())
    statuses: list[StatusItem] = Field(default_factory=list)
    forks: list[ForkItem] = Field(default_factory=list)
