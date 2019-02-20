import trio


async def loopy_child(number, lock):
    while True:
        async with lock:
            print("Child {} has the lock!".format(number))
            await trio.sleep(0.5)


async def main():
    async with trio.open_nursery() as nursery:
        lock = trio.Lock()
        nursery.start_soon(loopy_child, 1, lock)
        nursery.start_soon(loopy_child, 2, lock)

trio.run(main)
