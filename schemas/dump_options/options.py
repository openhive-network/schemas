from __future__ import annotations

from pathlib import Path  # noqa: TCH003

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
    value_type: Path | list[str] | str | bool | int
    default_value: Path | list[str] | str | bool | int


class Option(PreconfiguredBaseModel):
    name: str
    description: str
    value: OptionValue | None


class Options(PreconfiguredBaseModel):
    common: list[Option] | None
    config_file: list[Option] | None
    command_line: list[Option] | None
