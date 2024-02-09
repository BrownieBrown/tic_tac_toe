from enum import Enum, auto


class GameState(Enum):
    CONTINUE = auto()
    EXIT = auto()
    INVALID = auto()
    OCCUPIED = auto()
    VALID = auto()


class PlayerSymbol(Enum):
    PLAYER_1 = "X"
    PLAYER_2 = "O"


class BoardSymbol(Enum):
    EMPTY = " "
    VERTICAL = "|"
    HORIZONTAL = "-"
    PLAYER_1 = "X"
    PLAYER_2 = "O"


class Command(Enum):
    STATS = "p"
    EXIT = "e"
