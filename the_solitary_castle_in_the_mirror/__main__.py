from __future__ import annotations

import json
import sys
from argparse import ArgumentParser
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


def _build_whole_options_parser() -> ArgumentParser:
    options_parser = ArgumentParser(add_help=False)
    options_parser.add_argument(
        "--version", "-V", action="store_true", help="show version and exit"
    )
    return options_parser


def _build_main_parser(*, parents: list[ArgumentParser]) -> ArgumentParser:
    parser = ArgumentParser(parents=parents)
    parser.add_argument("character", nargs="+", choices=characters)
    return parser


def main() -> None:
    whole_options_parser = _build_whole_options_parser()
    options, unknown = whole_options_parser.parse_known_args()
    if options.version:
        print(__version__)
        sys.exit(0)

    parser = _build_main_parser(parents=[whole_options_parser])
    args = parser.parse_args(unknown)

    days = _main(args.character)

    print(json.dumps(days))


if __name__ == "__main__":
    main()
