from datetime import date

import pytest

import the_solitary_castle_in_the_mirror._date as sut


class Test_年を返す:
    class DateForTest(sut.CharacterDate):
        @staticmethod
        def the_year() -> int:
            return 2005

    @pytest.mark.parametrize("date_", [date(2023, 5, 1), date(2023, 12, 31)])
    def test_5月から12月はthe_yearの年を返す(self, date_):
        assert self.DateForTest.replace_year(date_) == 2005

    @pytest.mark.parametrize("date_", [date(2023, 1, 1), date(2023, 4, 30)])
    def test_1月から4月はthe_yearの翌年を返す(self, date_):
        assert self.DateForTest.replace_year(date_) == 2006


def test_こころちゃんのパラレルワールド():
    assert sut.DateInKokoroWorld.the_year() == 2005


def test_リオンくんのパラレルワールド():
    assert sut.DateInRionWorld.the_year() == 2005


def test_スバルくんのパラレルワールド():
    assert sut.DateInSubaruWorld.the_year() == 1984


def test_アキちゃんのパラレルワールド():
    assert sut.DateInAkiWorld.the_year() == 1991


def test_マサムネくんのパラレルワールド():
    assert sut.DateInMasamuneWorld.the_year() == 2012


def test_フウカちゃんのパラレルワールド():
    assert sut.DateInFukaWorld.the_year() == 2019


def test_ウレシノくんのパラレルワールド():
    assert sut.DateInUreshinoWorld.the_year() == 2026
