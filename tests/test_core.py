from datetime import date

import the_solitary_castle_in_the_mirror._date as d
import the_solitary_castle_in_the_mirror.core as sut


def test_パラレルワールドの曜日を返せる():
    assert sut.calculate_weekday("kokoro", date(2022, 12, 23)) == "Friday"


def test_キャラクターのパラレルワールドに変換できる():
    actual = sut.to_character_date(date(2022, 12, 23), "kokoro")
    expected = d.DateInKokoroWorld(date(2005, 12, 23))
    assert actual == expected
