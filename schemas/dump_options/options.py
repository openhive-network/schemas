from __future__ import annotations

from typing import Any

from schemas._preconfigured_base_model import PreconfiguredBaseModel

__all__ = [
    "OptionValue",
    "Option",
    "Options",
]


class OptionValue(PreconfiguredBaseModel):
    required: bool
    multitoken: bool
    composed: bool
    value_type: str
    default_value: Any
    fields_count: int | None = None


class Option(PreconfiguredBaseModel):
    name: str
    description: str
    value: OptionValue | None = None


class Options(PreconfiguredBaseModel):
    common: list[Option] | None = None
    config_file: list[Option] | None = None
    command_line: list[Option] | None = None
