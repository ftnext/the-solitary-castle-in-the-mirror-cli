from __future__ import annotations

from abc import ABCMeta, abstractmethod
from datetime import date

from the_solitary_castle_in_the_mirror._types import CharacterName


class CharacterDate(metaclass=ABCMeta):
    weekdays = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }

    def __init__(self, date_: date) -> None:
        self._date = date_

    @classmethod
    def create(cls, date_: date) -> CharacterDate:
        return cls(date_.replace(year=cls.the_year()))

    @staticmethod
    @abstractmethod
    def the_year() -> int:
        raise NotImplementedError

    def weekday(self) -> str:
        return self.weekdays[self._date.weekday()]


class DateInKokoroWorld(CharacterDate):
    @staticmethod
    def the_year() -> int:
        return 2005


class DateInRionWorld(CharacterDate):
    @staticmethod
    def the_year() -> int:
        return 2005


class DateInSubaruWorld(CharacterDate):
    @staticmethod
    def the_year() -> int:
        return 1984


class DateInAkiWorld(CharacterDate):
    @staticmethod
    def the_year() -> int:
        return 1991


class DateInMasamuneWorld(CharacterDate):
    @staticmethod
    def the_year() -> int:
        return 2012


class DateInFukaWorld(CharacterDate):
    @staticmethod
    def the_year() -> int:
        return 2019


class DateInUreshinoWorld(CharacterDate):
    @staticmethod
    def the_year() -> int:
        return 2026


_mappings: dict[CharacterName, type[CharacterDate]] = {
    CharacterName.KOKORO: DateInKokoroWorld,
    CharacterName.AKI: DateInAkiWorld,
    CharacterName.FUKA: DateInFukaWorld,
    CharacterName.RION: DateInRionWorld,
    CharacterName.SUBARU: DateInSubaruWorld,
    CharacterName.MASAMUNE: DateInMasamuneWorld,
    CharacterName.URESHINO: DateInUreshinoWorld,
}
