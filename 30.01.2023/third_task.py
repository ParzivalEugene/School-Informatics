def func(num: int, count_even: int = 0) -> int:
    """
    Return the number of ways to get 55 from 1 with use of no more than 15 even numbers.

    Args:
        num (int): The number to get 55 from.
        count_even (int): The number of even numbers.

    Returns:
        int: The number of ways to get 55 from 1 with use of no more than 15 even numbers.
    """
    if num > 55:
        return 0
    if num == 55:
        return count_even <= 15
    return sum(
        (
            func(num + 2, count_even + int(num % 2 == 0)),
            func(num + 3, count_even + int(num % 2 == 0)),
            func(num * 2 + 1, count_even + int(num % 2 == 0)),
        )
    )


print(func(1))
