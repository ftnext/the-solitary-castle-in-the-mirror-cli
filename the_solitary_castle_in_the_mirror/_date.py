from __future__ import annotations

from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from datetime import date
from types import MappingProxyType
from typing import cast

from the_solitary_castle_in_the_mirror._types import (
    CharacterNameEnum,
    Weekday,
    WeekdayInt,
)


class CharacterDate(metaclass=ABCMeta):
    weekdays: dict[WeekdayInt, Weekday] = {
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
        return cls(date_.replace(year=cls.replace_year(date_)))

    @classmethod
    def replace_year(cls, date_: date) -> int:
        if date_.month >= 5:
            return cls.the_year()
        else:
            return cls.the_year() + 1

    @staticmethod
    @abstractmethod
    def the_year() -> int:
        raise NotImplementedError

    def weekday(self) -> Weekday:
        return self.weekdays[cast(WeekdayInt, self._date.weekday())]


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


_mappings: MappingProxyType[
    CharacterNameEnum, type[CharacterDate]
] = MappingProxyType(
    {
        CharacterNameEnum.KOKORO: DateInKokoroWorld,
        CharacterNameEnum.AKI: DateInAkiWorld,
        CharacterNameEnum.FUKA: DateInFukaWorld,
        CharacterNameEnum.RION: DateInRionWorld,
        CharacterNameEnum.SUBARU: DateInSubaruWorld,
        CharacterNameEnum.MASAMUNE: DateInMasamuneWorld,
        CharacterNameEnum.URESHINO: DateInUreshinoWorld,
    }
)
