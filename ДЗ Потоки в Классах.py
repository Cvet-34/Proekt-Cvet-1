import threading
from threading import Thread  # класс Thread реализует нашу работу с потоками
from time import time, sleep


class Knight(Thread):

    def __init__(self, name, power):
        Thread.__init__(self)           #Инициализация потока
        self.name = name
        self.power = power

    def run(self):                      #Запуск потока
        n = 100
        print(f'{self.name}, на нас напали')
        day = 0
        print(f'Сражался:, {n // self.power}, дней')
        while n > 0:
            sleep(1)
            day += 1
            n = n - self.power
            print(f'{self.name}, сражался {day} день: осталось: {n} врагов')
        else:
            print('Сражение закончено, враг повержен!')

if __name__ == "__main__":
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()


