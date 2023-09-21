from __future__ import annotations


def snake_case_to_pascal_case(text: str) -> str:
    return "".join([segment.title() for segment in text.split("_")])
