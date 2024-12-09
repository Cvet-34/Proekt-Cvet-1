import threading                # модуль поток, с его помощью можно выполнять разные операции используя разные потоки
from queue import Queue         # очередь, Библеотека с инструментами для передачи информации между потоками
import random                   # модуль для генерации случайных чисел.
import time                     # операции со временем.

#Класс Table:
#Объекты этого класса должны создаваться следующим способом - Table(1)
#Обладать атрибутами number - номер стола и guest - гость, который сидит за этим столом (по умолчанию None)
class Table:
    def __init__(self, number):
        self.number = int(number)
        self.guest = None

#Класс Guest:
#Должен наследоваться от класса Thread (быть потоком).
#Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
#Обладать атрибутом name - имя гостя.
#Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.
class Guest(threading.Thread):          #класс Guest наследует из класса threading.Thread для создания потока
    def __init__(self, name):
        super().__init__()
        self.name = str(name)

    def run(self):
        time.sleep(random.randint(3, 10))   # случайное колличество секунд для задержки исполнения программы в диапазоне от 3-10

#Класс Cafe:
#Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
#Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
#Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

#Метод guest_arrival(self, *guests): Должен принимать неограниченное кол - во гостей(объектов класса Guest).
#Далее, если есть свободный стол, то садить гостя за стол(назначать столу guest), запускать поток гостя и
#выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
#Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue выводить сообщение"<имя гостя> в очереди".
    def guest_arrival(self, *guests):
        for guest in guests:
            table = self.free_table()
            if table:
                table.guest = guest
                guest.start()
                print(f'{guest.name} сел(а) за стол № {table.number}')
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

#Метод discuss_guests(self):
#Этот метод имитирует процесс обслуживания гостей.
#Обслуживание должно происходить пока очередь не пустая(метод empty) или хотя бы один стол занят.
#Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive), то
#вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен".Так
#же текущий стол освобождается(table.guest = None).
#Если очередь ещё не пуста(метод empty) и стол один из столов освободился(None), то текущему столу присваивается
#гость взятый из очереди(queue.get()).
#Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
#Далее запустить поток этого гостя(start)
    def discuss_guests(self):
        while not self.queue.empty() or self.guest_still_seated():          # ожидать, пока очередь не будет пустой
            for table in self.tables:                                       # проверяет, переберает столы
                if table.guest and not table.guest.is_alive():              # закончил ли гость приём пищи и завершил ли работу
                    print(f'{table.guest.name} покушал(а) и ушёл(ла)')    # стол гость ушел
                    print(f'Номер стола {table.number} свободен')           # стол совободен
                    table.guest = None

                if not self.queue.empty() and table.guest is None:
                    next_guest = self.queue.get()                           # приглашает нового гостя
                    table.guest = next_guest
                    next_guest.start()
                    print(f'{next_guest.name} вышел(ла) из очереди и сел(а) за стол № {table.number}')

    def free_table(self):               #проходит по всем столам в списке self.tables. Если у стола нет гостя,
        for table in self.tables:       #то метод возвращает сам стол, в противном случае — None.
            if table.guest is None:
                return table
        return None

    def guest_still_seated(self):
        return any(table.guest is not None for table in self.tables)   # есть ли кто то в очереди


tables = [Table(number) for number in range(1, 7)]

guests_names = ['Semin', 'Sacha', 'Timur', 'Roma', 'Sony', 'Andrey',
                'Elena', 'Larisa', 'Galina', 'Pavel', 'Natali']

guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()


#мы получаем 3 класса на основе которых имитируется работа кафе:
#Table - стол, хранит информацию о находящемся за ним гостем (Guest).
#Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
#Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival) и их обслуживания (discuss_guests).
