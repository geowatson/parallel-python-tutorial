import asyncio


async def factorial(number: int):
    f = 1
    await asyncio.sleep(1)
    for i in range(2, number + 1):
        # print(f"Task {name}: Compute factorial({i})...")
        f *= i
    print(f"factorial({number}) = {f}")


async def async_factorial(number_from: int,
                          number_to: int):
    await asyncio.gather(*(factorial(i) for i in range(number_from, number_to)))

# t = time()
asyncio.run(async_factorial(1000, 1002))
# print(time() - t)
from time import time
t = time()
print(time() - t)