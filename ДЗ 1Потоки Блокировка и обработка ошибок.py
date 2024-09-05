import threading
from threading import Thread, Lock
from time import time, sleep

x = 0
lock = Lock()


class Bank(Thread):

    def __init__(self, balance):
        Thread.__init__(self)
        self.balance = balance

    def deposit(self):
        global x
        e = self.balance
        bn = f'Запрос баланса на начало: {e}'
        print(bn)
        z = 68000
        popl = f'Пополнение баланса: {z}'
        print(popl)
        lock.acquire()
        self.balance = z + e
        lock.release()
        print(f'текуший Баланс после пополнения: {self.balance}')
        sleep(1)

    def take(self):
        global x
        e1 = self.balance
        bn1 = f'Запрос баланса на начало: {e1}'
        print(bn1)
        z1 = 58000
        popl1 = f'Снятие средств: {z1}'
        print(popl1)
        if self.balance < z1:
            print("Недостаточно средств")
        else:
            lock.acquire()
            x = e1 - z1
            lock.release()
            print(f'текуший Баланс после списания: {x}')
        sleep(1)


bk = Bank(0)


def potok():
    global x
    x = 0
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()


for i in range(100):
    potok()
    print(x)

print(f'Итоговый баланс: {x}')
