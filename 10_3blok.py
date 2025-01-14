import threading                        # библиотека с инструментами для создания потоков
import random                           # позволяет генерировать случайные числа
from threading import Thread, Lock      # импорт класса Thread и метод Lock для блокировки потоков
import time                             #sleep из библиотеки для созданию временной задержки для имитации выполнения работы потока.

#Атрибуты объекта:
#balance - баланс банка (int)
#lock - объект класса Lock для блокировки потоков.

class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

#Метод deposit:
    def deposit(self):
        for i in range(100):                                        #совершать 100 транзакций пополнения средств
            if self.balance >=500 and self.lock.locked():
                self.lock.release()                                     #разблокирован  методом release.
            a = random.randint(50,500)
            self.balance += a                                   # увеличение баланса на случайное целое число от 50 до 500
            print(f"Пополнение: {a}, Баланс: {self.balance}")
            time.sleep(0.001)                                   # ожидание в 0.001 секунды,имитация задержки выполнения пополнения.

#Метод take:
    def take(self):
        for i in range(100):                                     #совершать 100 транзакций пополнения средств
            b = random.randint(50,500)
            print(f"Запрос на {b}")
            if self.balance >= b:
                self.balance -= b                               # уменьшение баланса на случайное целое число от 50 до 500
                print(f"Снятие {b}, balans: {self.balance}")
            else:
                print("Запрос отклонен, недостаточно средство")
                self.lock.acquire()
            time.sleep(0.001)


#создаем объект класса Bank
bk = Bank()

#создаем 2 потока для методов deposit и take
# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th_deposit = threading.Thread(target=Bank.deposit, args=(bk,))
th_take = threading.Thread(target=Bank.take, args=(bk,))

# запуск потока
th_deposit.start()
th_take.start()
# дожидается выполнения работы предыдущего потока и затем запускается следующий, упорядочивает работу потоков.
th_deposit.join()
th_take.join()

print(f'Итоговый баланс: {bk.balance}')