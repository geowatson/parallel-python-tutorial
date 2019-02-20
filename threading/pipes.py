from multiprocessing import Pipe
from multiprocessing.connection import Connection

from threading import Thread
from time import sleep


def worker(conn: Connection, delay: int):
    sleep(delay)
    print("message from worker")
    print(conn.recv())


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    Thread(target=worker, args=(child_conn, 3)).start()
    parent_conn.send("data from main")
