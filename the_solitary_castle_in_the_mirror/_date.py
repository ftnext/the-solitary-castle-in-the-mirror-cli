from __future__ import annotations

from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
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


@dataclass(init=False)
class DateInKokoroWorld(CharacterDate):
    @staticmethod
    def the_year() -> int:
        return 2005


@dataclass(init=False)
class DateInRionWorld(CharacterDate):
    @staticmethod
    def the_year() -> int:
        return 2005


@dataclass(init=False)
class DateInSubaruWorld(CharacterDate):
    @staticmethod
    def the_year() -> int:
        return 1984


@dataclass(init=False)
class DateInAkiWorld(CharacterDate):
    @staticmethod
    def the_year() -> int:
        return 1991


@dataclass(init=False)
class DateInMasamuneWorld(CharacterDate):
    @staticmethod
    def the_year() -> int:
        return 2012


@dataclass(init=False)
class DateInFukaWorld(CharacterDate):
    @staticmethod
    def the_year() -> int:
        return 2019


@dataclass(init=False)
class DateInUreshinoWorld(CharacterDate):
    @staticmethod
    def the_year() -> int:
        return 2026


_mappings: dict[CharacterName, type[CharacterDate]] = {
    CharacterName.kokoro: DateInKokoroWorld,
    CharacterName.aki: DateInAkiWorld,
    CharacterName.fuka: DateInFukaWorld,
    CharacterName.rion: DateInRionWorld,
    CharacterName.subaru: DateInSubaruWorld,
    CharacterName.masamune: DateInMasamuneWorld,
    CharacterName.ureshino: DateInUreshinoWorld,
}
