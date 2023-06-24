from __future__ import annotations

from datetime import date

from the_solitary_castle_in_the_mirror._date import CharacterDate
from the_solitary_castle_in_the_mirror._date import _mappings as mappings
from the_solitary_castle_in_the_mirror._types import CharacterName


def calculate_weekday(character: str, date_: date) -> str:
    character_date = to_character_date(date_, character)
    return character_date.weekday()


def to_character_date(date_: date, character: str) -> CharacterDate:
    return mappings[CharacterName.from_str(character)].create(date_)
