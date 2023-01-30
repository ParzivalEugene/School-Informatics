from enum import Enum, auto


class Move(Enum):
    """
    Enum for moves
    """

    PLUS_ONE = auto()
    MULTIPLY_TWO = auto()
    START = ""


def func(
    num: int, current_move: Move = Move.START, previous_move: Move = Move.START
) -> int:
    """
    Return the number of ways to get 16 from 1 without two functions repeat in a row.

    Args:
        num (int): The number to get 16 from.
        current_move (Move): The current move.
        previous_move (Move): The previous move.

    Returns:
        int: The number of ways to get 16 from 1 without two functions repeat in a row.
    """
    if num > 16:
        return 0
    if num == 16:
        return 1
    if num < 16:
        if current_move == previous_move == Move.PLUS_ONE:
            return func(num * 2, Move.MULTIPLY_TWO, current_move)
        elif current_move == previous_move == Move.MULTIPLY_TWO:
            return func(num + 1, Move.PLUS_ONE, current_move)
        return func(num + 1, Move.PLUS_ONE, current_move) + func(
            num * 2, Move.MULTIPLY_TWO, current_move
        )


print(func(1))
