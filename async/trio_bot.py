import trio

from random import randint
from sys import version_info

n_consumers = 5
batch_size = 32


async def producer(send_channel):
    iteration = 0
    messages = ["hello", "howdy, programmer?", "farewell", "js sucks", "well done, Morty the bot!"]
    users_count = randint(0, 10)
    while True:
        messages_stream = [messages[randint(0, len(messages) - 1)]
                           for _ in range(users_count)]
        for index, message in enumerate(messages_stream):
            await send_channel.send(
                (message, iteration, index)
            )
        iteration += 1


async def consumer(receive_channel):
    # The consumer uses an 'async for' loop to receive the values:
    batch = []
    async for message, iteration, index in receive_channel:
        print(f"have message [{iteration}, {index}, {len(message)}]")
        if len(batch) < batch_size:
            batch.append(message)
        else:
            batch = []
            await trio.sleep(3)

        print(f"processing of [{iteration}, {index}, {len(message)}] complete")


async def main():
    async with trio.open_nursery() as nursery:
        send_channel, receive_channel = trio.open_memory_channel(0)
        for _ in range(n_consumers):
            nursery.start_soon(consumer, receive_channel)
        nursery.start_soon(producer, send_channel)

trio.run(main)


if __name__ == '__main__':
    assert version_info >= (3, 7), "Script requires Python 3.7+."
    trio.run(main)