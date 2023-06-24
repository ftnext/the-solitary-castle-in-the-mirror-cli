from __future__ import annotations

from enum import Enum, auto
from typing import Literal, cast

Character = Literal[
    "kokoro", "aki", "fuka", "rion", "subaru", "masamune", "ureshino"
]


class CharacterName(Enum):
    KOKORO = auto()
    AKI = auto()
    FUKA = auto()
    RION = auto()
    SUBARU = auto()
    MASAMUNE = auto()
    URESHINO = auto()

    @classmethod
    def from_lower(cls, lower: Character) -> CharacterName:
        """
        >>> CharacterName.from_lower("kokoro") is CharacterName.KOKORO
        True
        """
        return cls[lower.upper()]

    def __str__(self) -> Character:
        """
        >>> print(CharacterName.KOKORO)
        kokoro
        """
        return cast(Character, f"{self.name.lower()}")
