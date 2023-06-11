from __future__ import annotations

import argparse
from datetime import date
import json

from the_solitary_castle_in_the_mirror.core import to_character_date
from the_solitary_castle_in_the_mirror.constants import characters


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("character", nargs="+", choices=characters)
    args = parser.parse_args()

    today = date.today()
    days: dict[str, str] = {}
    for character in args.character:
        character_date = to_character_date(today, character)
        days[character] = character_date.weekday()

    print(json.dumps(days))


if __name__ == "__main__":
    main()
