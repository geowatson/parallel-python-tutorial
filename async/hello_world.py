import asyncio

from sys import version_info


async def hello():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')


# Python 3.7+
async def main():
    return await asyncio.gather(
        hello(),
        hello())

if __name__ == "__main__":
    assert version_info >= (3, 7), "Script requires Python 3.7+."
    asyncio.run(main())
