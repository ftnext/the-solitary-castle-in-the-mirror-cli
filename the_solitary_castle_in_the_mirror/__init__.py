from typing import cast

from the_solitary_castle_in_the_mirror._types import (
    Character,
    CharacterNameEnum,
)

characters: list[Character] = cast(
    list[Character],
    [str(value) for value in CharacterNameEnum.__members__.values()],
)
