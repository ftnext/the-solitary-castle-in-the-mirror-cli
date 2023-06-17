import the_solitary_castle_in_the_mirror._date as sut


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
