from __future__ import annotations

from enum import Enum, auto
from typing import Literal, cast

Character = Literal[
    "kokoro", "aki", "fuka", "rion", "subaru", "masamune", "ureshino"
]


class CharacterNameEnum(Enum):
    KOKORO = auto()
    AKI = auto()
    FUKA = auto()
    RION = auto()
    SUBARU = auto()
    MASAMUNE = auto()
    URESHINO = auto()

    @classmethod
    def from_lower(cls, lower: Character) -> CharacterNameEnum:
        """
        >>> CharacterNameEnum.from_lower("kokoro") is CharacterNameEnum.KOKORO
        True
        """
        return cls[lower.upper()]

    def __str__(self) -> Character:
        """
        >>> print(CharacterNameEnum.KOKORO)
        kokoro
        """
        return cast(Character, f"{self.name.lower()}")
