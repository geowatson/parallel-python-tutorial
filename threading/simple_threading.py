from threading import Thread
from time import sleep


def worker(delay: int):
    sleep(delay)
    print("message from worker")


if __name__ == '__main__':
    Thread(target=worker, args=(3, )).start()
    print("message from main")