from freezegun import freeze_time

from the_solitary_castle_in_the_mirror.__main__ import _main


@freeze_time("2022-12-23")
def test_それぞれのパラレルワールドの曜日を返せる():
    the_seven = [
        "kokoro",
        "rion",
        "aki",
        "fuka",
        "subaru",
        "masamune",
        "ureshino",
    ]
    expected = {
        "kokoro": "Friday",
        "rion": "Friday",
        "aki": "Monday",
        "fuka": "Monday",
        "subaru": "Sunday",
        "masamune": "Sunday",
        "ureshino": "Wednesday",
    }

    actual = _main(the_seven)
    assert actual == expected
    assert (
        the_seven == [name for name in actual] == [name for name in expected]
    )
