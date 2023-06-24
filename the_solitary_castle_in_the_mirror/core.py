from __future__ import annotations

from datetime import date

from the_solitary_castle_in_the_mirror._date import CharacterDate
from the_solitary_castle_in_the_mirror._date import _mappings as mappings
from the_solitary_castle_in_the_mirror._types import Character, CharacterName


def calculate_weekday(character: Character, date_: date) -> str:
    character_date = to_character_date(date_, character)
    return character_date.weekday()


def to_character_date(date_: date, character: Character) -> CharacterDate:
    return mappings[CharacterName.from_lower(character)].create(date_)
