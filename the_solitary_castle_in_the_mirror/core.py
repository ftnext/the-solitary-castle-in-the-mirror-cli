from __future__ import annotations

from datetime import date
from the_solitary_castle_in_the_mirror._date import (
    CharacterDate,
    _mappings as mappings,
)


def to_character_date(date_: date, character: str) -> CharacterDate:
    return mappings[character].create(date_)
