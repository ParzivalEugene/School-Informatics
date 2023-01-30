def func(
    num: int,
    first_command: bool = False,
    second_command: bool = False,
    third_command: bool = False,
) -> int:
    """
    Return the number of ways to get 25 from 3 with use of all commands.

    Args:
        num (int): The number to get 25 from.
        first_command (bool): The first command.
        second_command (bool): The second command.
        third_command (bool): The third command.

    Returns:
        int: The number of ways to get 25 from 3 with use of all commands.
    """
    if num > 25:
        return 0
    if num == 25:
        return all([first_command, second_command, third_command])
    return sum(
        (
            func(num + 1, True, second_command, third_command),
            func(num + 2, first_command, True, third_command),
            func(num * 2, first_command, second_command, True),
        )
    )


print(func(3))
