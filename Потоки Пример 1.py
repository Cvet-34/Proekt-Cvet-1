#Многопоточность.
from threading import  # Библиотека поддерживает создание потков
from datetime import datetime #Библиотека создает метод создания подсчета времени выполнения команды
import requests #Библиотека для это библиотека, которая предоставляет возможность
# http://...-запросами при помощи языка Python. нужно скачать.


time_start = datetime.now()
THE_URL = 'http:/.....'
res = []


def func(url):
    respons = requests.get(THE_URL)
    page_response = response.json()
    res.append(page_response)


thr_first = Thread(target=func, args=(THE_URL )) # готовится поток. поток будет выполнять функцию
thr_second = Thread(target=func, args=(THE_URL ))
thr_third = Thread(target=func, args=(THE_URL ))

thr_first.start() # Запустили потоки в работу
thr_second.start()
thr_second.start()

thr_first.join() # Контролирует поток и дожидается окончания
thr_second.join()
thr_second.join()

time_end = datetime.now()
time_res = time_end - time_start # замерили время выполнениея программы
print(time_res)
print(res)