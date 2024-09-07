import pandas as pd
import numpy as np
import requests
from envoy import Response

# импорт pandas. создание аналитической таблицы с данными.
#создать словарь
#передать словарь в качестве аргумента в метод DataFrame()
#распечатать DataFrame.

pddf = pd.DataFrame({"Океаны Земли": ['Тихий океан', 'Атлантический океан', 'Индийский океан',
                                      'Северный ледовитый океан', 'Южный океан'],

                     "Величина %": ['Самый большой', 'Второй по величина', 'Третий по величине', 'Пятый по величине',
                                    'Четвертый по величине'],

                     "Размер млн.кв.км": [178.6, 91.7, 76.2, 14.7, 20.3],

                     "Объем воды млн км³": [710.36, 329.66, 282.65, 18.07, 71.00]})
print(pddf)


#import numpy

# одномерный массив
a = np.array([1, 2, 3])
print(a)

#Многомерный массив
a = np.array([[22, 34, 35], [10, 15, 16]])
print(a)

a = np.random.random((4, 7))
print(a)
print(a.sum())

#создаем массив с помощью функции np.array()
a = np.array([5, 10, 15, 20, 25])
b = np.array([0, 1, 2, 3, 4])
c = a - b  #разница двух массивов
print(c)


# импорт requests:
requests.get(
    'https://github.com/Cvet-34/Proekt-Cvet-1/blob/main/ДЗ%20НОВ.Декораторы.py')  # запрос и получение ответа на запрос.
print(Response, [200]) 

response = requests.get(
    r'https://github.com/Cvet-34/Proekt-Cvet-1/blob/main/ДЗ%20НОВ.Декораторы.py')  # получение текста после запроса текста
response.encoding = 'utf-8'
print(response.text)
