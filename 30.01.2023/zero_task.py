def func(n: int) -> int:
    """
    Return the nth sequence number.

    Args:
        n (int): The index of the sequence number.

    Returns:
        int: The nth sequence number.
    """
    if data[n] != -1:
        return data[n]

    result = 0
    if n % 2 == 0:
        result += func(n // 2)
    result += func(n - 3)
    data[n] = result
    return data[n]


data = [-1] * (63 + 1)
data[:8] = [0, 0, 0, 1, 0, 0, 2, 1]
func(27)
data[:27] = [0] * 27
print(func(63))
