from typing import cast

from the_solitary_castle_in_the_mirror._types import Character, CharacterName

characters: list[Character] = cast(
    list[Character],
    [str(value) for value in CharacterName.__members__.values()],
)
