from freezegun import freeze_time

from the_solitary_castle_in_the_mirror.__main__ import _main


class Test_それぞれのパラレルワールドの曜日を返せる:
    the_seven = [
        "kokoro",
        "rion",
        "aki",
        "fuka",
        "subaru",
        "masamune",
        "ureshino",
    ]

    @freeze_time("2022-12-23")
    def test_5月から12月(self):
        expected = {
            "kokoro": "Friday",
            "rion": "Friday",
            "aki": "Monday",
            "fuka": "Monday",
            "subaru": "Sunday",
            "masamune": "Sunday",
            "ureshino": "Wednesday",
        }

        actual = _main(self.the_seven)
        assert actual == expected
        assert (
            self.the_seven
            == [name for name in actual]
            == [name for name in expected]
        )

    @freeze_time("2023-01-10")
    def test_1月から4月(self):
        expected = {
            "kokoro": "Tuesday",
            "rion": "Tuesday",
            "aki": "Friday",
            "fuka": "Friday",
            "subaru": "Thursday",
            "masamune": "Thursday",
            "ureshino": "Sunday",
        }

        actual = _main(self.the_seven)
        assert actual == expected
        assert (
            self.the_seven
            == [name for name in actual]
            == [name for name in expected]
        )
