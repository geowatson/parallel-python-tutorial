from multiprocessing import Process
from threading import Thread
from queue import Queue
from pprint import pprint
from time import sleep, time


def f(q):
    while True:
        content = q.get()
        print(content)


if __name__ == '__main__':
    s = 10
    t = time()
    q = Queue(s * 2)
    p = [Thread(target=f, args=(q,), daemon=True) for i in range(s)]
    [p.start() for p in p]
    while True:
        [q.put("some content") for i in range(s)]
        sleep(2)
        print("---")
