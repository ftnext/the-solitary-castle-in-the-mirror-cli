from __future__ import annotations

import argparse
import json
from datetime import date

from the_solitary_castle_in_the_mirror import characters
from the_solitary_castle_in_the_mirror.core import calculate_weekday


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("character", nargs="+", choices=characters)
    args = parser.parse_args()

    today = date.today()
    days: dict[str, str] = {}
    for character in args.character:
        days[character] = calculate_weekday(character, today)

    print(json.dumps(days))


if __name__ == "__main__":
    main()
