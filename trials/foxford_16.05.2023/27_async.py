from math import ceil
import asyncio
import time

global_store = []


async def count_price(data, i):
    i = data[i][0]
    if len(global_store) % 1000 == 0:
        print(f"CHECKPOINT: {len(global_store)}")
    return sum([abs(km - i) * boxes for km, boxes in data])


async def count_part(data, _from, _to):
    for i in range(_from, _to):
        global_store.append(await count_price(data, i))


async def main():
    with open("data/27_B.txt", encoding="utf-8") as file:
        n, *data = list(map(lambda x: list(map(int, x.split())), file.readlines()))
        data, n = [[i, ceil(v / 30)] for i, v in data], n[0]

        k = 100
        part = n // k
        parts = [(part * i, part * (i + 1)) for i in range(k)]  # 7879886864050
        parts[-1] = (parts[-1][0], parts[-1][1] + 1)

        await asyncio.gather(*[count_part(data, x, y) for x, y in parts])
        print(min(global_store))


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"Executed in {elapsed:0.2f} seconds.")
