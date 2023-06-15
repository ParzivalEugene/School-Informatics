# 1000000 2000000
import asyncio


async def check(n):
    divisors = []
    i = 1
    while i <= n / i:
        if n % i == 0:
            divisors.append(i)
            if i != n / i:
                divisors.append(int(n / i))
        i += 1
    return len([i for i in divisors if i % 2 == 0]) == 5


async def count(a, b):
    for i in range(a, b):
        if await check(i):
            print(i)


async def main():
    await asyncio.gather(
        *[
            count(x, y)
            for x, y in (
                (1000000, 1033333),
                (1033333, 1066666),
                (1066666, 1099999),
                (1099999, 1133332),
                (1133332, 1166665),
                (1166665, 1199998),
                (1199998, 1233331),
                (1233331, 1266664),
                (1266664, 1299997),
                (1299997, 1333330),
                (1333330, 1366663),
                (1366663, 1399996),
                (1399996, 1433329),
                (1433329, 1466662),
                (1466662, 1499995),
                (1499995, 1533328),
                (1533328, 1566661),
                (1566661, 1599994),
                (1599994, 1633327),
                (1633327, 1666660),
                (1666660, 1699993),
                (1699993, 1733326),
                (1733326, 1766659),
                (1766659, 1799992),
                (1799992, 1833325),
                (1833325, 1866658),
                (1866658, 1899991),
                (1899991, 1933324),
                (1933324, 1966657),
                (1966657, 2000000),
            )
        ]
    )


if __name__ == "__main__":
    import time

    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
