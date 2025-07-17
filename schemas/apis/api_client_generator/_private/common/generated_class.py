from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import ast


@dataclass
class GeneratedClass:
    """Represents a generated class with its definition and imports."""

    class_def: ast.ClassDef
    imports: list[ast.ImportFrom]
