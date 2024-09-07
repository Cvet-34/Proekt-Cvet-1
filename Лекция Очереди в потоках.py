from threading import Thread
import queue
from time import sleep


def producer(queue):
    c = 0
    while True:
        c +=1
        message = 'ping' + str(c)
        queue.put(message)
        sleep(1)


def worker(queue):
    while True:
        message = queue.get()
        print(message)


q = queue.Queue()
tr1 = Thread(target=producer, args=(q,))
tr2 = Thread(target=worker, args=(q,))

tr1.start()
tr2.start()

tr1.join()
tr2.join()
