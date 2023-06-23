from __future__ import annotations

from enum import Enum, auto


class CharacterName(Enum):
    kokoro = auto()
    aki = auto()
    fuka = auto()
    rion = auto()
    subaru = auto()
    masamune = auto()
    ureshino = auto()

    @classmethod
    def from_str(cls, name: str) -> CharacterName:
        """
        >>> CharacterName.from_str("kokoro") is CharacterName.kokoro
        True
        """
        return {n: v for n, v in cls.__members__.items()}[name]
