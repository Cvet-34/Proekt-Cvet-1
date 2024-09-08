import inspect
from pprint import pprint

import requests


def introspection_info(obj):
    return obj


class Fmn:
    def __init__(self, *ags):
        self.ags = ags
        a = []
        for i in self.ags:
            a = i
            if a == 30:
                print('верно')
            else:
                print('не верно')


fmn = Fmn(52, 30)

print(fmn)

number_info = introspection_info(42)
print(number_info)
func = introspection_info


print('Выясняем тип-класс передаваемого объекта obj:')
print(type(number_info)) # узнали тип передаваемого аргумента
print(type(number_info) is int) # проверили к типу int относиться передаваемый аргумент получили True
print(type(number_info) is list) # проверили к типу list относится передаваемый аргумент получили False
print('Для запоменания материала:')
print(type(requests)) # получили тип <class 'module'>
print(type(requests.get)) # проверили get получилиclass <'function'>

print('С помощью выясняем какие атрибуты и методы можно применять к:')
print('Передаваемый объект obj:')
print(dir(number_info))
print('для Функции:')
print(dir(introspection_info))
print('для класса:')
print(dir(Fmn))

print('Имя функции, класса, библиотеки, функции сохраненной в переменную:')
print(introspection_info.__name__) #  имя функции вывели в консоль
print(Fmn.__name__) # имя класса в консоль
print(requests.__name__) # обратились и вывели имя библиотеки
print(func.__name__) # сохранили функцию в переменную, через переменную имя функции узнали

print('Проверяем объекты с помощью inspect:')

print(inspect.ismodule(number_info)) # это не модуль, получили False
print(inspect.ismodule(requests)) # это модуль, получили True
print(inspect.isclass(Fmn)) # это класс, получили True
print(inspect.isfunction(introspection_info)) # это функция, получили True
print(inspect.isbuiltin(requests)) # это не встроенный модуль, нужно скачивать получили False

print('С помощью isinstance мы можем определить является ли объект экземпляром класса:')
print(isinstance(number_info, str))
print(isinstance(number_info, int))
print(isinstance(number_info, Fmn)) # number_info не является экземпляром класса, получили False
print(isinstance(fmn, Fmn))

print('с помощью callable выясняем вызываемый ли это объект:')
print(callable(number_info)) # не вызываемый, получили False
print(callable(introspection_info))  #функция вызываемый объект, получили True