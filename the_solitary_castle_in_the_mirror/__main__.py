from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Iterable
from datetime import date

from the_solitary_castle_in_the_mirror import (
    Character,
    Weekday,
    __version__,
    calculate_weekday,
    characters,
)


def _main(characters: Iterable[Character]) -> dict[Character, Weekday]:
    today = date.today()
    days: dict[Character, Weekday] = {}
    for character in characters:
        days[character] = calculate_weekday(character, today)
    return days


def main() -> None:
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument(
        "--version", "-V", action="store_true", help="show version and exit"
    )
    pre_args, unknown = pre_parser.parse_known_args()
    if pre_args.version:
        print(__version__)
        sys.exit(0)

    parser = argparse.ArgumentParser(parents=[pre_parser])
    parser.add_argument("character", nargs="+", choices=characters)
    args = parser.parse_args(unknown)

    days = _main(args.character)

    print(json.dumps(days))


if __name__ == "__main__":
    main()
