from __future__ import annotations

from enum import Enum, auto
from typing import Literal, cast

Character = Literal[
    "kokoro", "aki", "fuka", "rion", "subaru", "masamune", "ureshino"
]
Weekday = Literal[
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
WeekdayInt = Literal[0, 1, 2, 3, 4, 5, 6]


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
