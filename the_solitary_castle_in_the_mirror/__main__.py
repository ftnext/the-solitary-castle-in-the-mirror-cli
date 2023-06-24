from __future__ import annotations

import argparse
import json
from collections.abc import Iterable
from datetime import date

from the_solitary_castle_in_the_mirror import characters
from the_solitary_castle_in_the_mirror._types import Character
from the_solitary_castle_in_the_mirror.core import calculate_weekday


def _main(characters: Iterable[Character]) -> dict[Character, str]:
    today = date.today()
    days: dict[Character, str] = {}
    for character in characters:
        days[character] = calculate_weekday(character, today)
    return days


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("character", nargs="+", choices=characters)
    args = parser.parse_args()

    days = _main(args.character)

    print(json.dumps(days))


if __name__ == "__main__":
    main()
