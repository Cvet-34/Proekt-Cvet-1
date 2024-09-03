from threading import Thread  # Библиотека
from datetime import datetime  # Библиотека для создания метода подсчета времени выполнения команды
from time import sleep #sleep берем из библиотека для созданию временной задержки выполнения потока.


def white_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file_name: #Открываем файл
        for i in range(word_count):
            file_name.write(f'Какое-то слово № {i + 1}\n') # Загружаем в файл слова
            sleep(0.1)                                      # работа потоков выполнена с задержкой 0.1с
        print(f'Завершилась запись в файл {file_name}')


example1 = Thread(target=white_words, args=(10, 'example1.txt', )) # готовится поток. поток будет выполнять функцию
example2 = Thread(target=white_words, args=(30, 'example2.txt', )) # поток, к какой ункции обращаемся, аргументы для работы
example3 = Thread(target=white_words, args=(200, 'example3.txt', ))
example4 = Thread(target=white_words, args=(100, 'example4.txt', ))

example5 = Thread(target=white_words, args=(10, 'example5.txt')) # готовится поток. поток будет выполнять функцию
example6 = Thread(target=white_words, args=(30, 'example6.txt'))
example7 = Thread(target=white_words, args=(200, 'example7.txt'))
example8 = Thread(target=white_words, args=(100, 'example8.txt'))

time_start = datetime.now()
example1.start()  # Запустили потоки в работу
example2.start()
example3.start()
example4.start()

time_start1 = datetime.now()
example5.start()  # Запустили потоки в работу
example6.start()
example7.start()
example8.start()

example1.join()  # Контролирует поток и дожидается окончания
example2.join()
example3.join()
example4.join()
time_end = datetime.now()
time_res = time_end - time_start

example5.join()# Контролирует поток и дожидается окончания
example6.join()
example7.join()
example8.join()
time_end1 = datetime.now()
time_res1 = time_end1 - time_start1  # замерили время окончание выполнения программы

print('Время выполнения работы потоков с 1 по 4 потоков', time_res)
print('Время выполнения работы потоков с 5 по 8 потоков', time_res1)




