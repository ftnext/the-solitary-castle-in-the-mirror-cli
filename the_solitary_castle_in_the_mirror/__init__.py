from typing import cast

from the_solitary_castle_in_the_mirror._types import Weekday  # NOQA: F401
from the_solitary_castle_in_the_mirror._types import (
    Character,
    CharacterNameEnum,
)
from the_solitary_castle_in_the_mirror.core import (  # NOQA: F401
    calculate_weekday,
)

__version__ = "0.1.0"

characters: list[Character] = cast(
    list[Character],
    [str(value) for value in CharacterNameEnum.__members__.values()],
)
