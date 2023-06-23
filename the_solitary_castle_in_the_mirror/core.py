from __future__ import annotations

from datetime import date

from the_solitary_castle_in_the_mirror._date import CharacterDate
from the_solitary_castle_in_the_mirror._date import _mappings as mappings
from the_solitary_castle_in_the_mirror._types import CharacterName


def to_character_date(date_: date, character: str) -> CharacterDate:
    return mappings[CharacterName.from_str(character)].create(date_)
